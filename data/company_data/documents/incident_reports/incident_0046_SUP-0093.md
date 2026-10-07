# Shipment Incident INC-2026-0046

Incident ID: INC-2026-0046
Supplier: Shenzhen MicroSystems Germany
Supplier ID: SUP-0093
Component: Printed Circuit Board Module 378
Component ID: CMP-0378
Origin Country: Germany
Origin Port: Hamburg
Delay Days: 4
Delay Reason: capacity shortage
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as capacity shortage. The affected component is
Printed Circuit Board Module 378. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Nova Health Monitor 38, Zenith Edge Server 24.
Single-source product-component mappings for this component: 1.
The incident can create customer-service exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Hamburg have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Shenzhen MicroSystems Germany; component Printed Circuit Board Module 378; country Germany; port Hamburg; delay 4 days; reason capacity shortage; escalation watch.
