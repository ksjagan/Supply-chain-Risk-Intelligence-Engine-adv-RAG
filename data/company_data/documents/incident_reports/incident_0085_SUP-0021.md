# Shipment Incident INC-2026-0085

Incident ID: INC-2026-0085
Supplier: Mekong Materials Germany
Supplier ID: SUP-0021
Component: Power Electronics Module 029
Component ID: CMP-0029
Origin Country: Germany
Origin Port: Hamburg
Delay Days: 9
Delay Reason: compliance documentation gap
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as compliance documentation gap. The affected component is
Power Electronics Module 029. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 52, Helios Energy Controller 11, Pulse Wearable Dock 01, Vega Retail Sensor 70.
Single-source product-component mappings for this component: 1.
The incident can create regulatory hold risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- check high-revenue products using the affected component
- Ask logistics to validate whether other shipments from Hamburg have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Mekong Materials Germany; component Power Electronics Module 029; country Germany; port Hamburg; delay 9 days; reason compliance documentation gap; escalation amber.
