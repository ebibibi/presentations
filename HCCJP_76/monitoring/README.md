# Azure Monitor availability experiment

The HCCJP 76 demo uses Azure-native monitoring instead of a custom dashboard.

## Intended flow

1. An on-premises Linux or Windows server is represented in Azure by Azure Arc.
2. Its web endpoint is published without an inbound firewall rule or public IP.
3. An Application Insights Standard availability test checks the endpoint.
4. The audience sees the standard Azure Monitor Availability and alert views turn red.
5. The AI investigates Azure Monitor evidence and uses Azure Arc Run Command to restore the service.
6. The same availability test proves recovery when the view returns to green.

## Detection characteristics

- Azure Arc machine status is not the web-service signal. The Connected Machine agent sends a
  heartbeat every five minutes, and Arc normally changes a machine to `Disconnected` only after
  15-30 minutes without heartbeats.
- The Standard availability test is the correct end-to-end HTTP signal. Its minimum/default
  interval is 300 seconds, so expected detection is roughly 0-5 minutes plus alert-processing
  latency.
- A Standard test requires a publicly reachable URL. A server public IP is not required:
  Cloudflare Tunnel publishes the private origin over outbound HTTPS.
- Standard test executions are billed. Do not enable the Bicep deployment without explicit cost
  approval.

## Temporary Quick Tunnel (experiment only)

The `.sh` helpers manage `arclnx01` through a transient systemd service. The `.ps1` helpers manage
`arcwin01` through a SYSTEM scheduled task. Both install `cloudflared` when necessary and start a
temporary `trycloudflare.com` URL. Generated hostnames change after restart and have no production
SLA, so use them only to prove the monitoring path.

Send the script through Azure Arc Run Command. Base64 is used deliberately: passing a multiline
script directly through Bash, Azure CLI, ARM, and the guest handler can collapse quoting or
newlines.

```bash
payload="$(base64 -w0 start-cloudflare-quick.sh)"
az connectedmachine run-command create \
  --name hccjp76-cloudflare-quick \
  --machine-name arclnx01 \
  --resource-group rg-hccjp76-arc \
  --location japaneast \
  --script "echo '$payload' | base64 -d >/tmp/hccjp76-cloudflare-quick.sh; bash /tmp/hccjp76-cloudflare-quick.sh"
```

Stop the temporary endpoint after the experiment:

```bash
payload="$(base64 -w0 stop-cloudflare-quick.sh)"
az connectedmachine run-command create \
  --name hccjp76-cloudflare-quick-stop \
  --machine-name arclnx01 \
  --resource-group rg-hccjp76-arc \
  --location japaneast \
  --script "echo '$payload' | base64 -d >/tmp/hccjp76-cloudflare-quick-stop.sh; bash /tmp/hccjp76-cloudflare-quick-stop.sh"
```

## Event-day endpoint

A named Cloudflare Tunnel with a stable hostname under `ebisuda.net` is **not available**: the zone is
authoritative on Azure DNS, and a public hostname for a Cloudflare Tunnel resolves only through
Cloudflare's own authoritative servers (`<tunnel-id>.cfargotunnel.com`). A CNAME written in Azure DNS
does not resolve. Use the Quick Tunnel on the day and publish the generated URL through
`../links.json` (see `../run-of-show.md`, section 1.5). A stable name would require delegating a
subdomain zone such as `lab.ebisuda.net` to Cloudflare.

Keep the origin private and accept only outbound HTTPS from `cloudflared`. The Azure Monitor test
should validate both HTTP 200 and unique page content so a generic proxy error cannot be mistaken
for success.

## Azure Monitor deployment

`main.bicep` creates a Log Analytics workspace, workspace-based Application Insights, a Standard
availability test, and a metric alert. Paid test execution is disabled by default. Compile and
preview it without enabling the test:

```bash
az bicep build --file main.bicep
az deployment group what-if \
  --resource-group rg-hccjp76-arc \
  --template-file main.bicep \
  --parameters \
    linuxEndpointUrl='https://linux-example.trycloudflare.com' \
    windowsEndpointUrl='https://windows-example.trycloudflare.com'
```

After explicit cost approval, enable the test:

```bash
az deployment group create \
  --resource-group rg-hccjp76-arc \
  --template-file main.bicep \
  --parameters \
    linuxEndpointUrl='https://linux-example.trycloudflare.com' \
    windowsEndpointUrl='https://windows-example.trycloudflare.com' \
    monitoringEnabled=true
```

The experiment uses one Japan test location and alerts after one failed location to minimize live
demo latency. A production configuration should use at least five locations and normally require
three failures, as recommended by Microsoft.

Delete only these temporary monitoring resources while preserving the resource group and Arc
machines:

```bash
./cleanup-azure.sh
```

## Current deployment (2026-08-13 JST)

Deployed with `monitoringEnabled=true` against the live Quick Tunnel URLs. Both tests report 100%
availability from Japan East. Billing is active: **JPY 0.1173 per Standard Web Test execution**
(Japan East retail price) x 288/day x 2 tests = **about JPY 68/day**. Run `cleanup-azure.sh` after
the event.

If a Quick Tunnel is restarted its hostname changes, so the web test `RequestUrl` must be
redeployed as well — otherwise the tests go red against a dead URL before the demo even starts.
See `../run-of-show.md`, section 1.6.

## Verified experiment (2026-08-05 JST)

Both endpoints were monitored from Azure Monitor Japan East with a 300-second Standard test.

| Event | Linux / nginx | Windows / IIS |
|---|---:|---:|
| Healthy baseline | 17:46, 100% | 17:46, 100% |
| Service stopped through Arc Run Command | 17:51:03 | 17:51:46 |
| Public endpoint response after stop | HTTP 502 | HTTP 502 |
| Failed availability sample | 17:55, 0% | 17:55, 0% |
| Active Azure Monitor alert fired | 17:57:15 | 17:57:13 |
| Stop-to-alert duration | **6m 12s** | **5m 27s** |
| Service restored through Arc Run Command | 17:58:59 | 17:59:33 |
| Healthy availability sample | 18:00, 100% | 18:00, 100% |
| Alert auto-resolved | 18:04:15 | 18:04:15 |

After validation, all six temporary Azure monitoring resources were deleted. Both Quick Tunnels,
scheduled jobs, downloaded `cloudflared` binaries, and temporary files were also removed. Final
state: both Arc machines `Connected`; nginx and W3SVC running; local HTTP 200 on both servers; no
Monitor/OperationalInsights resources remaining in `rg-hccjp76-arc`.
