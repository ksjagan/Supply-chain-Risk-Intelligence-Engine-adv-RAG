# Shipment Incident INC-2026-0075

Incident ID: INC-2026-0075
Supplier: Shenzhen Components Mexico
Supplier ID: SUP-0109
Component: Connectivity Module Module 165
Component ID: CMP-0165
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 10
Delay Reason: commodity price volatility
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as commodity price volatility. The affected component is
Connectivity Module Module 165. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 74, Helios Energy Controller 43, Zenith Edge Server 03.
Single-source product-component mappings for this component: 0.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- check high-revenue products using the affected component
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Shenzhen Components Mexico; component Connectivity Module Module 165; country Mexico; port Manzanillo; delay 10 days; reason commodity price volatility; escalation amber.
