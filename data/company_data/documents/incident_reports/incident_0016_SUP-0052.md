# Shipment Incident INC-2026-0016

Incident ID: INC-2026-0016
Supplier: Delta Optics South Korea
Supplier ID: SUP-0052
Component: Semiconductor Module 262
Component ID: CMP-0262
Origin Country: South Korea
Origin Port: Busan
Delay Days: 12
Delay Reason: commodity price volatility
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as commodity price volatility. The affected component is
Semiconductor Module 262. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Helios Energy Controller 53, Vega Retail Sensor 78.
Single-source product-component mappings for this component: 2.
The incident can create regulatory hold risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Busan have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Delta Optics South Korea; component Semiconductor Module 262; country South Korea; port Busan; delay 12 days; reason commodity price volatility; escalation amber.
