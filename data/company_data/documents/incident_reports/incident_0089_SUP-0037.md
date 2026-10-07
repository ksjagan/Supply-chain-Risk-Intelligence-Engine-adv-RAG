# Shipment Incident INC-2026-0089

Incident ID: INC-2026-0089
Supplier: Vertex Foundry Mexico
Supplier ID: SUP-0037
Component: Printed Circuit Board Module 026
Component ID: CMP-0026
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 11
Delay Reason: compliance documentation gap
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as compliance documentation gap. The affected component is
Printed Circuit Board Module 026. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 21, Vega Retail Sensor 80, Zenith Edge Server 07.
Single-source product-component mappings for this component: 1.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- review active shipments from the same origin port
- confirm open purchase orders due in the next 45 days
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Vertex Foundry Mexico; component Printed Circuit Board Module 026; country Mexico; port Manzanillo; delay 11 days; reason compliance documentation gap; escalation amber.
