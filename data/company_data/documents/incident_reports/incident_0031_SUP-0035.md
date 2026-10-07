# Shipment Incident INC-2026-0031

Incident ID: INC-2026-0031
Supplier: Azura Optics Turkey
Supplier ID: SUP-0035
Component: Display Module Module 317
Component ID: CMP-0317
Origin Country: Turkey
Origin Port: Mersin
Delay Days: 21
Delay Reason: compliance documentation gap
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as compliance documentation gap. The affected component is
Display Module Module 317. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 69, Zenith Edge Server 66.
Single-source product-component mappings for this component: 1.
The incident can create customer-service exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- check high-revenue products using the affected component
- Ask logistics to validate whether other shipments from Mersin have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Azura Optics Turkey; component Display Module Module 317; country Turkey; port Mersin; delay 21 days; reason compliance documentation gap; escalation red.
