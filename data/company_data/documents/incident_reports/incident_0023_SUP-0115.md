# Shipment Incident INC-2026-0023

Incident ID: INC-2026-0023
Supplier: Taiwan Assembly Germany
Supplier ID: SUP-0115
Component: Sensor Module 085
Component ID: CMP-0085
Origin Country: Germany
Origin Port: Hamburg
Delay Days: 12
Delay Reason: labor disruption
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as labor disruption. The affected component is
Sensor Module 085. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 51, Vega Retail Sensor 28, Zenith Edge Server 06.
Single-source product-component mappings for this component: 1.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- check high-revenue products using the affected component
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Hamburg have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Taiwan Assembly Germany; component Sensor Module 085; country Germany; port Hamburg; delay 12 days; reason labor disruption; escalation amber.
