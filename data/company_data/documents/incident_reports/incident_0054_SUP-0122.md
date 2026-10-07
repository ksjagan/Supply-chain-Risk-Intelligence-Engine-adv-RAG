# Shipment Incident INC-2026-0054

Incident ID: INC-2026-0054
Supplier: Nordic Assembly Poland
Supplier ID: SUP-0122
Component: Battery Module 380
Component ID: CMP-0380
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 12
Delay Reason: customs inspection delays
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as customs inspection delays. The affected component is
Battery Module 380. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 46, Pulse Wearable Dock 01, Zenith Edge Server 03.
Single-source product-component mappings for this component: 2.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- compare the issue against the last three supplier scorecards
- check high-revenue products using the affected component
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Nordic Assembly Poland; component Battery Module 380; country Poland; port Gdansk; delay 12 days; reason customs inspection delays; escalation amber.
