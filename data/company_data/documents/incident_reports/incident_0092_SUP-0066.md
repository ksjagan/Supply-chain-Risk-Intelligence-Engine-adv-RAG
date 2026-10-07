# Shipment Incident INC-2026-0092

Incident ID: INC-2026-0092
Supplier: Shenzhen Assembly Poland
Supplier ID: SUP-0066
Component: Display Module Module 310
Component ID: CMP-0310
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 24
Delay Reason: labor disruption
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as labor disruption. The affected component is
Display Module Module 310. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 51.
Single-source product-component mappings for this component: 0.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- check high-revenue products using the affected component
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Shenzhen Assembly Poland; component Display Module Module 310; country Poland; port Gdansk; delay 24 days; reason labor disruption; escalation red.
