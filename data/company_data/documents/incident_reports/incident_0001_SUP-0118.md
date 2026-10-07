# Shipment Incident INC-2026-0001

Incident ID: INC-2026-0001
Supplier: Apex Assembly Turkey
Supplier ID: SUP-0118
Component: Connectivity Module Module 337
Component ID: CMP-0337
Origin Country: Turkey
Origin Port: Mersin
Delay Days: 16
Delay Reason: commodity price volatility
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as commodity price volatility. The affected component is
Connectivity Module Module 337. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 10, Orion Smart Hub 75, Pulse Wearable Dock 76.
Single-source product-component mappings for this component: 0.
The incident can create regulatory hold risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- check high-revenue products using the affected component
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Mersin have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Apex Assembly Turkey; component Connectivity Module Module 337; country Turkey; port Mersin; delay 16 days; reason commodity price volatility; escalation red.
