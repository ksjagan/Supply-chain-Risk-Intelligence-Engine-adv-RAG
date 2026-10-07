# Shipment Incident INC-2026-0071

Incident ID: INC-2026-0071
Supplier: Nordic Assembly Poland
Supplier ID: SUP-0122
Component: Battery Module 115
Component ID: CMP-0115
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 24
Delay Reason: commodity price volatility
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as commodity price volatility. The affected component is
Battery Module 115. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 12, Nova Health Monitor 33, Nova Health Monitor 35, Pulse Wearable Dock 49, Zenith Edge Server 03.
Single-source product-component mappings for this component: 1.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- check high-revenue products using the affected component
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Nordic Assembly Poland; component Battery Module 115; country Poland; port Gdansk; delay 24 days; reason commodity price volatility; escalation red.
