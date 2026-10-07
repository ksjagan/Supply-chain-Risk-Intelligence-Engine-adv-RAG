# Shipment Incident INC-2026-0026

Incident ID: INC-2026-0026
Supplier: Delta Materials Turkey
Supplier ID: SUP-0038
Component: Battery Module 380
Component ID: CMP-0380
Origin Country: Turkey
Origin Port: Mersin
Delay Days: 24
Delay Reason: customs inspection delays
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as customs inspection delays. The affected component is
Battery Module 380. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 46, Pulse Wearable Dock 01, Zenith Edge Server 03.
Single-source product-component mappings for this component: 2.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- ask planning to model a two-week supply interruption
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Mersin have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Delta Materials Turkey; component Battery Module 380; country Turkey; port Mersin; delay 24 days; reason customs inspection delays; escalation red.
