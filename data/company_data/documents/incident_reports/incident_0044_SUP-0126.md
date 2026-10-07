# Shipment Incident INC-2026-0044

Incident ID: INC-2026-0044
Supplier: Nova MicroSystems China
Supplier ID: SUP-0126
Component: Sensor Module 089
Component ID: CMP-0089
Origin Country: China
Origin Port: Yantian
Delay Days: 5
Delay Reason: port congestion
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Sensor Module 089. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 21, Nova Health Monitor 79, Orion Smart Hub 37.
Single-source product-component mappings for this component: 0.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- confirm open purchase orders due in the next 45 days
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Yantian have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Nova MicroSystems China; component Sensor Module 089; country China; port Yantian; delay 5 days; reason port congestion; escalation watch.
