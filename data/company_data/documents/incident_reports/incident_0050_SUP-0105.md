# Shipment Incident INC-2026-0050

Incident ID: INC-2026-0050
Supplier: Azura MicroSystems Poland
Supplier ID: SUP-0105
Component: Battery Module 170
Component ID: CMP-0170
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 4
Delay Reason: capacity shortage
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as capacity shortage. The affected component is
Battery Module 170. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 42, Helios Energy Controller 41, Nova Health Monitor 35, Nova Health Monitor 47, Pulse Wearable Dock 15, Pulse Wearable Dock 25.
Single-source product-component mappings for this component: 0.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- compare the issue against the last three supplier scorecards
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Azura MicroSystems Poland; component Battery Module 170; country Poland; port Gdansk; delay 4 days; reason capacity shortage; escalation watch.
