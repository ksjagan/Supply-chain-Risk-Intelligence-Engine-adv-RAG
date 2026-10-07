# Shipment Incident INC-2026-0063

Incident ID: INC-2026-0063
Supplier: Mekong Assembly Malaysia
Supplier ID: SUP-0060
Component: Semiconductor Module 222
Component ID: CMP-0222
Origin Country: Malaysia
Origin Port: Port Klang
Delay Days: 3
Delay Reason: compliance documentation gap
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as compliance documentation gap. The affected component is
Semiconductor Module 222. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 08, Nova Health Monitor 63.
Single-source product-component mappings for this component: 1.
The incident can create customer-service exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- validate whether alternate suppliers are production-qualified
- Ask logistics to validate whether other shipments from Port Klang have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Mekong Assembly Malaysia; component Semiconductor Module 222; country Malaysia; port Port Klang; delay 3 days; reason compliance documentation gap; escalation watch.
