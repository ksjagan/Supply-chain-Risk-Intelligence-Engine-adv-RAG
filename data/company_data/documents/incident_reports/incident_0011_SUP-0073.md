# Shipment Incident INC-2026-0011

Incident ID: INC-2026-0011
Supplier: Delta Components Mexico
Supplier ID: SUP-0073
Component: Semiconductor Module 190
Component ID: CMP-0190
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 13
Delay Reason: geopolitical export controls
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as geopolitical export controls. The affected component is
Semiconductor Module 190. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Zenith Edge Server 56.
Single-source product-component mappings for this component: 0.
The incident can create regulatory hold risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- confirm open purchase orders due in the next 45 days
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Delta Components Mexico; component Semiconductor Module 190; country Mexico; port Manzanillo; delay 13 days; reason geopolitical export controls; escalation amber.
