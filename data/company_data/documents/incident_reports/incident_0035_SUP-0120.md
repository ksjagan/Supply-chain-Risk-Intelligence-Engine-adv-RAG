# Shipment Incident INC-2026-0035

Incident ID: INC-2026-0035
Supplier: Korea Assembly Mexico
Supplier ID: SUP-0120
Component: Semiconductor Module 158
Component ID: CMP-0158
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 22
Delay Reason: port congestion
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Semiconductor Module 158. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Pulse Wearable Dock 25, Zenith Edge Server 56.
Single-source product-component mappings for this component: 2.
The incident can create premium freight exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- check high-revenue products using the affected component
- confirm open purchase orders due in the next 45 days
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Korea Assembly Mexico; component Semiconductor Module 158; country Mexico; port Manzanillo; delay 22 days; reason port congestion; escalation red.
