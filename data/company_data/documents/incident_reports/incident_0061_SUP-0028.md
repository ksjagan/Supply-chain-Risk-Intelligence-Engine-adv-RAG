# Shipment Incident INC-2026-0061

Incident ID: INC-2026-0061
Supplier: Shenzhen Assembly Mexico
Supplier ID: SUP-0028
Component: Printed Circuit Board Module 361
Component ID: CMP-0361
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 7
Delay Reason: compliance documentation gap
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as compliance documentation gap. The affected component is
Printed Circuit Board Module 361. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Orion Smart Hub 40.
Single-source product-component mappings for this component: 1.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- ask planning to model a two-week supply interruption
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Shenzhen Assembly Mexico; component Printed Circuit Board Module 361; country Mexico; port Manzanillo; delay 7 days; reason compliance documentation gap; escalation watch.
