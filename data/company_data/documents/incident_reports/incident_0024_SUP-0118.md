# Shipment Incident INC-2026-0024

Incident ID: INC-2026-0024
Supplier: Apex Assembly Turkey
Supplier ID: SUP-0118
Component: Connectivity Module Module 384
Component ID: CMP-0384
Origin Country: Turkey
Origin Port: Mersin
Delay Days: 17
Delay Reason: port congestion
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Connectivity Module Module 384. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 46.
Single-source product-component mappings for this component: 0.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Mersin have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Apex Assembly Turkey; component Connectivity Module Module 384; country Turkey; port Mersin; delay 17 days; reason port congestion; escalation red.
