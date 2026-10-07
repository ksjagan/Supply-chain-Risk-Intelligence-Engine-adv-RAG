# Shipment Incident INC-2026-0091

Incident ID: INC-2026-0091
Supplier: Taiwan Circuits India
Supplier ID: SUP-0045
Component: Printed Circuit Board Module 305
Component ID: CMP-0305
Origin Country: India
Origin Port: Nhava Sheva
Delay Days: 18
Delay Reason: capacity shortage
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as capacity shortage. The affected component is
Printed Circuit Board Module 305. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Helios Energy Controller 23.
Single-source product-component mappings for this component: 0.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- validate whether alternate suppliers are production-qualified
- Ask logistics to validate whether other shipments from Nhava Sheva have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Taiwan Circuits India; component Printed Circuit Board Module 305; country India; port Nhava Sheva; delay 18 days; reason capacity shortage; escalation red.
