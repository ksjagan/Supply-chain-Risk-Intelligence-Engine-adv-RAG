# Shipment Incident INC-2026-0028

Incident ID: INC-2026-0028
Supplier: Korea Assembly Mexico
Supplier ID: SUP-0120
Component: Semiconductor Module 072
Component ID: CMP-0072
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 6
Delay Reason: capacity shortage
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as capacity shortage. The affected component is
Semiconductor Module 072. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 51.
Single-source product-component mappings for this component: 0.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- compare the issue against the last three supplier scorecards
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Korea Assembly Mexico; component Semiconductor Module 072; country Mexico; port Manzanillo; delay 6 days; reason capacity shortage; escalation watch.
