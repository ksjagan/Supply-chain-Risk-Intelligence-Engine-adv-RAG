# Shipment Incident INC-2026-0090

Incident ID: INC-2026-0090
Supplier: Korea Components Mexico 108
Supplier ID: SUP-0108
Component: Connectivity Module Module 327
Component ID: CMP-0327
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 15
Delay Reason: compliance documentation gap
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as compliance documentation gap. The affected component is
Connectivity Module Module 327. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 69, Helios Energy Controller 71.
Single-source product-component mappings for this component: 1.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- review active shipments from the same origin port
- check high-revenue products using the affected component
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Korea Components Mexico 108; component Connectivity Module Module 327; country Mexico; port Manzanillo; delay 15 days; reason compliance documentation gap; escalation red.
