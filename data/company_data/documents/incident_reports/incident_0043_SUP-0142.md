# Shipment Incident INC-2026-0043

Incident ID: INC-2026-0043
Supplier: Nova Foundry China
Supplier ID: SUP-0142
Component: Semiconductor Module 032
Component ID: CMP-0032
Origin Country: China
Origin Port: Yantian
Delay Days: 21
Delay Reason: capacity shortage
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as capacity shortage. The affected component is
Semiconductor Module 032. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 39, Nova Health Monitor 05, Orion Smart Hub 09, Zenith Edge Server 17.
Single-source product-component mappings for this component: 1.
The incident can create regulatory hold risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- review active shipments from the same origin port
- confirm open purchase orders due in the next 45 days
- Ask logistics to validate whether other shipments from Yantian have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Nova Foundry China; component Semiconductor Module 032; country China; port Yantian; delay 21 days; reason capacity shortage; escalation red.
