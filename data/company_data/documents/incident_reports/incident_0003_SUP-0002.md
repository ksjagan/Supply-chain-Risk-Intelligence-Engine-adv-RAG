# Shipment Incident INC-2026-0003

Incident ID: INC-2026-0003
Supplier: Nova MicroSystems Vietnam
Supplier ID: SUP-0002
Component: Power Electronics Module 154
Component ID: CMP-0154
Origin Country: Vietnam
Origin Port: Cat Lai
Delay Days: 9
Delay Reason: quality escape
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as quality escape. The affected component is
Power Electronics Module 154. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Zenith Edge Server 07.
Single-source product-component mappings for this component: 1.
The incident can create regulatory hold risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Cat Lai have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Nova MicroSystems Vietnam; component Power Electronics Module 154; country Vietnam; port Cat Lai; delay 9 days; reason quality escape; escalation amber.
