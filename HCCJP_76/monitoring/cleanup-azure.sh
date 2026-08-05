#!/usr/bin/env bash
# Delete only the temporary Azure Monitor resources created by main.bicep.
# The resource group and Azure Arc machines are deliberately preserved.
set -euo pipefail

subscription="${AZURE_SUBSCRIPTION_ID:-b0f2ddcb-c22b-4728-89b3-26e90a494ae4}"
resource_group="${AZURE_RESOURCE_GROUP:-rg-hccjp76-arc}"
base="/subscriptions/${subscription}/resourceGroups/${resource_group}/providers"

delete_if_present() {
  local id="$1"
  if az resource show --ids "$id" -o none 2>/dev/null; then
    az resource delete --ids "$id"
  fi
}

delete_if_present "${base}/Microsoft.Insights/metricAlerts/hccjp76-arclnx01-web-failed"
delete_if_present "${base}/Microsoft.Insights/metricAlerts/hccjp76-arcwin01-web-failed"
delete_if_present "${base}/Microsoft.Insights/webtests/hccjp76-arclnx01-web"
delete_if_present "${base}/Microsoft.Insights/webtests/hccjp76-arcwin01-web"
delete_if_present "${base}/Microsoft.Insights/components/appi-hccjp76-web"

if az monitor log-analytics workspace show \
  --subscription "$subscription" \
  --resource-group "$resource_group" \
  --workspace-name log-hccjp76 -o none 2>/dev/null; then
  az monitor log-analytics workspace delete \
    --subscription "$subscription" \
    --resource-group "$resource_group" \
    --workspace-name log-hccjp76 \
    --force true \
    --yes
fi

remaining="$(az resource list \
  --subscription "$subscription" \
  --resource-group "$resource_group" \
  --query "[?contains(type, 'Insights') || contains(type, 'OperationalInsights')].name" \
  -o tsv)"

if [[ -n "$remaining" ]]; then
  printf 'Unexpected monitoring resources remain:\n%s\n' "$remaining" >&2
  exit 1
fi

printf 'Temporary Azure Monitor resources removed; Azure Arc machines preserved.\n'
