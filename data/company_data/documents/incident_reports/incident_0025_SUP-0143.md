# Shipment Incident INC-2026-0025

Incident ID: INC-2026-0025
Supplier: Korea Materials Germany 143
Supplier ID: SUP-0143
Component: Printed Circuit Board Module 128
Component ID: CMP-0128
Origin Country: Germany
Origin Port: Hamburg
Delay Days: 15
Delay Reason: port congestion
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Printed Circuit Board Module 128. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 21, Nova Health Monitor 68, Pulse Wearable Dock 76, Zenith Edge Server 03.
Single-source product-component mappings for this component: 2.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- confirm open purchase orders due in the next 45 days
- Ask logistics to validate whether other shipments from Hamburg have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Korea Materials Germany 143; component Printed Circuit Board Module 128; country Germany; port Hamburg; delay 15 days; reason port congestion; escalation red.
