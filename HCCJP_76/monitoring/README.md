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

`start-cloudflare-quick.sh` installs `cloudflared` on `arclnx01` when necessary and starts a
temporary `trycloudflare.com` URL as a transient systemd service. Its generated hostname changes
after restart and has no production SLA, so use it only to prove the monitoring path.

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

Replace the Quick Tunnel with a named Cloudflare Tunnel and a stable DNS name. Keep the origin
private and accept only outbound HTTPS from `cloudflared`. The Azure Monitor test should validate
both HTTP 200 and unique page content so a generic proxy error cannot be mistaken for success.

## Azure Monitor deployment

`main.bicep` creates a Log Analytics workspace, workspace-based Application Insights, a Standard
availability test, and a metric alert. Paid test execution is disabled by default. Compile and
preview it without enabling the test:

```bash
az bicep build --file main.bicep
az deployment group what-if \
  --resource-group rg-hccjp76-arc \
  --template-file main.bicep \
  --parameters endpointUrl='https://example.trycloudflare.com'
```

After explicit cost approval, enable the test:

```bash
az deployment group create \
  --resource-group rg-hccjp76-arc \
  --template-file main.bicep \
  --parameters endpointUrl='https://example.trycloudflare.com' monitoringEnabled=true
```

The experiment uses one Japan test location and alerts after one failed location to minimize live
demo latency. A production configuration should use at least five locations and normally require
three failures, as recommended by Microsoft.
