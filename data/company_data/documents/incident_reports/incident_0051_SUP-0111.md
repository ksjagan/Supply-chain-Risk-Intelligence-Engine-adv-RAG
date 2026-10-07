# Shipment Incident INC-2026-0051

Incident ID: INC-2026-0051
Supplier: Taiwan MicroSystems Germany
Supplier ID: SUP-0111
Component: Connectivity Module Module 286
Component ID: CMP-0286
Origin Country: Germany
Origin Port: Hamburg
Delay Days: 9
Delay Reason: port congestion
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Connectivity Module Module 286. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 64, Nova Health Monitor 44, Zenith Edge Server 56, Zenith Edge Server 72.
Single-source product-component mappings for this component: 0.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- compare the issue against the last three supplier scorecards
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Hamburg have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Taiwan MicroSystems Germany; component Connectivity Module Module 286; country Germany; port Hamburg; delay 9 days; reason port congestion; escalation amber.
