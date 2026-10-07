# Shipment Incident INC-2026-0002

Incident ID: INC-2026-0002
Supplier: Apex Assembly Turkey
Supplier ID: SUP-0118
Component: Connectivity Module Module 138
Component ID: CMP-0138
Origin Country: Turkey
Origin Port: Mersin
Delay Days: 13
Delay Reason: commodity price volatility
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as commodity price volatility. The affected component is
Connectivity Module Module 138. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Pulse Wearable Dock 60.
Single-source product-component mappings for this component: 0.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- check high-revenue products using the affected component
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Mersin have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Apex Assembly Turkey; component Connectivity Module Module 138; country Turkey; port Mersin; delay 13 days; reason commodity price volatility; escalation amber.
