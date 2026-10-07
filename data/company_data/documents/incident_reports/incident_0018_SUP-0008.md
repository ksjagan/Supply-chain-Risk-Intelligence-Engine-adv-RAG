# Shipment Incident INC-2026-0018

Incident ID: INC-2026-0018
Supplier: Apex Electronics Poland
Supplier ID: SUP-0008
Component: Mechanical Housing Module 010
Component ID: CMP-0010
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 23
Delay Reason: customs inspection delays
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as customs inspection delays. The affected component is
Mechanical Housing Module 010. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Vega Retail Sensor 28.
Single-source product-component mappings for this component: 1.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- compare the issue against the last three supplier scorecards
- check high-revenue products using the affected component
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Apex Electronics Poland; component Mechanical Housing Module 010; country Poland; port Gdansk; delay 23 days; reason customs inspection delays; escalation red.
