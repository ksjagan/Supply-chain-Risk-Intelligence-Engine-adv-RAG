# Shipment Incident INC-2026-0098

Incident ID: INC-2026-0098
Supplier: Delta Precision Poland 44
Supplier ID: SUP-0044
Component: Power Electronics Module 144
Component ID: CMP-0144
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 7
Delay Reason: labor disruption
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as labor disruption. The affected component is
Power Electronics Module 144. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Orion Smart Hub 09, Pulse Wearable Dock 48, Zenith Edge Server 20.
Single-source product-component mappings for this component: 1.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Delta Precision Poland 44; component Power Electronics Module 144; country Poland; port Gdansk; delay 7 days; reason labor disruption; escalation watch.
