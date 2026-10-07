# Shipment Incident INC-2026-0037

Incident ID: INC-2026-0037
Supplier: Nordic Assembly Poland
Supplier ID: SUP-0122
Component: Battery Module 364
Component ID: CMP-0364
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 22
Delay Reason: customs inspection delays
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as customs inspection delays. The affected component is
Battery Module 364. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Helios Energy Controller 41.
Single-source product-component mappings for this component: 0.
The incident can create premium freight exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- check high-revenue products using the affected component
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Nordic Assembly Poland; component Battery Module 364; country Poland; port Gdansk; delay 22 days; reason customs inspection delays; escalation red.
