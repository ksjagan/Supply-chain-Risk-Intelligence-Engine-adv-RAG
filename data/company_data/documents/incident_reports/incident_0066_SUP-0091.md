# Shipment Incident INC-2026-0066

Incident ID: INC-2026-0066
Supplier: Mekong Cells Germany
Supplier ID: SUP-0091
Component: Printed Circuit Board Module 351
Component ID: CMP-0351
Origin Country: Germany
Origin Port: Hamburg
Delay Days: 14
Delay Reason: quality escape
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as quality escape. The affected component is
Printed Circuit Board Module 351. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Helios Energy Controller 23, Zenith Edge Server 20.
Single-source product-component mappings for this component: 1.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Hamburg have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Mekong Cells Germany; component Printed Circuit Board Module 351; country Germany; port Hamburg; delay 14 days; reason quality escape; escalation red.
