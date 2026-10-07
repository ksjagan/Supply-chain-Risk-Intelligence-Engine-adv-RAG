# Shipment Incident INC-2026-0027

Incident ID: INC-2026-0027
Supplier: Shenzhen Components Mexico
Supplier ID: SUP-0109
Component: Connectivity Module Module 178
Component ID: CMP-0178
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 18
Delay Reason: compliance documentation gap
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as compliance documentation gap. The affected component is
Connectivity Module Module 178. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 04, Orion Smart Hub 13, Orion Smart Hub 62, Pulse Wearable Dock 67.
Single-source product-component mappings for this component: 2.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- compare the issue against the last three supplier scorecards
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Shenzhen Components Mexico; component Connectivity Module Module 178; country Mexico; port Manzanillo; delay 18 days; reason compliance documentation gap; escalation red.
