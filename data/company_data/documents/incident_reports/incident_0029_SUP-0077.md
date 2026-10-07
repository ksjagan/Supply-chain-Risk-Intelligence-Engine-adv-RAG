# Shipment Incident INC-2026-0029

Incident ID: INC-2026-0029
Supplier: Mekong Circuits Turkey
Supplier ID: SUP-0077
Component: Printed Circuit Board Module 266
Component ID: CMP-0266
Origin Country: Turkey
Origin Port: Mersin
Delay Days: 24
Delay Reason: customs inspection delays
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as customs inspection delays. The affected component is
Printed Circuit Board Module 266. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Nova Health Monitor 33, Orion Smart Hub 62, Pulse Wearable Dock 50.
Single-source product-component mappings for this component: 0.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Mersin have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Mekong Circuits Turkey; component Printed Circuit Board Module 266; country Turkey; port Mersin; delay 24 days; reason customs inspection delays; escalation red.
