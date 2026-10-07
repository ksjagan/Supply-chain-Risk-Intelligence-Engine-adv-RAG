# Shipment Incident INC-2026-0070

Incident ID: INC-2026-0070
Supplier: Delta Optics South Korea
Supplier ID: SUP-0052
Component: Semiconductor Module 233
Component ID: CMP-0233
Origin Country: South Korea
Origin Port: Busan
Delay Days: 13
Delay Reason: port congestion
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Semiconductor Module 233. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Nova Health Monitor 35, Pulse Wearable Dock 01.
Single-source product-component mappings for this component: 1.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Busan have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Delta Optics South Korea; component Semiconductor Module 233; country South Korea; port Busan; delay 13 days; reason port congestion; escalation amber.
