# Shipment Incident INC-2026-0060

Incident ID: INC-2026-0060
Supplier: Bharat Cells Taiwan
Supplier ID: SUP-0145
Component: Connectivity Module Module 176
Component ID: CMP-0176
Origin Country: Taiwan
Origin Port: Kaohsiung
Delay Days: 8
Delay Reason: compliance documentation gap
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as compliance documentation gap. The affected component is
Connectivity Module Module 176. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Nova Health Monitor 65, Pulse Wearable Dock 26.
Single-source product-component mappings for this component: 0.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Kaohsiung have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Bharat Cells Taiwan; component Connectivity Module Module 176; country Taiwan; port Kaohsiung; delay 8 days; reason compliance documentation gap; escalation amber.
