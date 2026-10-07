# Shipment Incident INC-2026-0074

Incident ID: INC-2026-0074
Supplier: Azura Components China
Supplier ID: SUP-0128
Component: Battery Module 065
Component ID: CMP-0065
Origin Country: China
Origin Port: Yantian
Delay Days: 23
Delay Reason: port congestion
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Battery Module 065. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Zenith Edge Server 72.
Single-source product-component mappings for this component: 0.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- review active shipments from the same origin port
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Yantian have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Azura Components China; component Battery Module 065; country China; port Yantian; delay 23 days; reason port congestion; escalation red.
