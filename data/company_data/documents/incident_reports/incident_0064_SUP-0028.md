# Shipment Incident INC-2026-0064

Incident ID: INC-2026-0064
Supplier: Shenzhen Assembly Mexico
Supplier ID: SUP-0028
Component: Printed Circuit Board Module 090
Component ID: CMP-0090
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 10
Delay Reason: customs inspection delays
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as customs inspection delays. The affected component is
Printed Circuit Board Module 090. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 12, Helios Energy Controller 11, Orion Smart Hub 62, Pulse Wearable Dock 48, Zenith Edge Server 07.
Single-source product-component mappings for this component: 2.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- ask planning to model a two-week supply interruption
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Shenzhen Assembly Mexico; component Printed Circuit Board Module 090; country Mexico; port Manzanillo; delay 10 days; reason customs inspection delays; escalation amber.
