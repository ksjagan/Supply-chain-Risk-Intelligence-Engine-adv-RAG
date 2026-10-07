# Shipment Incident INC-2026-0069

Incident ID: INC-2026-0069
Supplier: Apex Cells India
Supplier ID: SUP-0127
Component: Power Electronics Module 247
Component ID: CMP-0247
Origin Country: India
Origin Port: Nhava Sheva
Delay Days: 18
Delay Reason: port congestion
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Power Electronics Module 247. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 61, Helios Energy Controller 71, Pulse Wearable Dock 67, Vega Retail Sensor 30.
Single-source product-component mappings for this component: 2.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Nhava Sheva have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Apex Cells India; component Power Electronics Module 247; country India; port Nhava Sheva; delay 18 days; reason port congestion; escalation red.
