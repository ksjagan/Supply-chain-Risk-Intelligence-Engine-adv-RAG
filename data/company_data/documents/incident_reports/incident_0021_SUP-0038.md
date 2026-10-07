# Shipment Incident INC-2026-0021

Incident ID: INC-2026-0021
Supplier: Delta Materials Turkey
Supplier ID: SUP-0038
Component: Battery Module 380
Component ID: CMP-0380
Origin Country: Turkey
Origin Port: Mersin
Delay Days: 9
Delay Reason: labor disruption
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as labor disruption. The affected component is
Battery Module 380. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 46, Pulse Wearable Dock 01, Zenith Edge Server 03.
Single-source product-component mappings for this component: 2.
The incident can create customer-service exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- review active shipments from the same origin port
- confirm open purchase orders due in the next 45 days
- Ask logistics to validate whether other shipments from Mersin have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Delta Materials Turkey; component Battery Module 380; country Turkey; port Mersin; delay 9 days; reason labor disruption; escalation amber.
