# Shipment Incident INC-2026-0039

Incident ID: INC-2026-0039
Supplier: Nordic Assembly Taiwan
Supplier ID: SUP-0042
Component: Sensor Module 294
Component ID: CMP-0294
Origin Country: Taiwan
Origin Port: Kaohsiung
Delay Days: 8
Delay Reason: port congestion
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Sensor Module 294. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 08, Atlas Robotics Kit 52, Pulse Wearable Dock 60, Zenith Edge Server 34.
Single-source product-component mappings for this component: 1.
The incident can create regulatory hold risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- ask planning to model a two-week supply interruption
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Kaohsiung have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Nordic Assembly Taiwan; component Sensor Module 294; country Taiwan; port Kaohsiung; delay 8 days; reason port congestion; escalation amber.
