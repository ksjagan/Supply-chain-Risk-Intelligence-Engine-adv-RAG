# Shipment Incident INC-2026-0059

Incident ID: INC-2026-0059
Supplier: Apex Assembly Turkey
Supplier ID: SUP-0118
Component: Connectivity Module Module 146
Component ID: CMP-0146
Origin Country: Turkey
Origin Port: Mersin
Delay Days: 18
Delay Reason: customs inspection delays
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as customs inspection delays. The affected component is
Connectivity Module Module 146. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Nova Health Monitor 47, Orion Smart Hub 55.
Single-source product-component mappings for this component: 0.
The incident can create customer-service exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Mersin have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Apex Assembly Turkey; component Connectivity Module Module 146; country Turkey; port Mersin; delay 18 days; reason customs inspection delays; escalation red.
