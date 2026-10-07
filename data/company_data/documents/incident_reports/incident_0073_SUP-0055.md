# Shipment Incident INC-2026-0073

Incident ID: INC-2026-0073
Supplier: Vertex Components South Korea
Supplier ID: SUP-0055
Component: Sensor Module 340
Component ID: CMP-0340
Origin Country: South Korea
Origin Port: Busan
Delay Days: 8
Delay Reason: quality escape
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as quality escape. The affected component is
Sensor Module 340. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 42, Nova Health Monitor 05.
Single-source product-component mappings for this component: 0.
The incident can create customer-service exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- ask planning to model a two-week supply interruption
- confirm open purchase orders due in the next 45 days
- Ask logistics to validate whether other shipments from Busan have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Vertex Components South Korea; component Sensor Module 340; country South Korea; port Busan; delay 8 days; reason quality escape; escalation amber.
