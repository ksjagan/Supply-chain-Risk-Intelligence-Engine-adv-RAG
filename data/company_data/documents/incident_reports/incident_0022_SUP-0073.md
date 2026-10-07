# Shipment Incident INC-2026-0022

Incident ID: INC-2026-0022
Supplier: Delta Components Mexico
Supplier ID: SUP-0073
Component: Semiconductor Module 312
Component ID: CMP-0312
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 22
Delay Reason: customs inspection delays
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as customs inspection delays. The affected component is
Semiconductor Module 312. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Helios Energy Controller 23, Pulse Wearable Dock 01.
Single-source product-component mappings for this component: 2.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Delta Components Mexico; component Semiconductor Module 312; country Mexico; port Manzanillo; delay 22 days; reason customs inspection delays; escalation red.
