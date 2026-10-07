# Shipment Incident INC-2026-0019

Incident ID: INC-2026-0019
Supplier: Vertex Foundry China
Supplier ID: SUP-0017
Component: Battery Module 021
Component ID: CMP-0021
Origin Country: China
Origin Port: Yantian
Delay Days: 12
Delay Reason: commodity price volatility
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as commodity price volatility. The affected component is
Battery Module 021. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Helios Energy Controller 41, Vega Retail Sensor 30.
Single-source product-component mappings for this component: 1.
The incident can create premium freight exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Yantian have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Vertex Foundry China; component Battery Module 021; country China; port Yantian; delay 12 days; reason commodity price volatility; escalation amber.
