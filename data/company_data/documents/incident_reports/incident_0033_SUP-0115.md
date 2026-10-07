# Shipment Incident INC-2026-0033

Incident ID: INC-2026-0033
Supplier: Taiwan Assembly Germany
Supplier ID: SUP-0115
Component: Sensor Module 089
Component ID: CMP-0089
Origin Country: Germany
Origin Port: Hamburg
Delay Days: 7
Delay Reason: labor disruption
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as labor disruption. The affected component is
Sensor Module 089. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 21, Nova Health Monitor 79, Orion Smart Hub 37.
Single-source product-component mappings for this component: 0.
The incident can create customer-service exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- compare the issue against the last three supplier scorecards
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Hamburg have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Taiwan Assembly Germany; component Sensor Module 089; country Germany; port Hamburg; delay 7 days; reason labor disruption; escalation watch.
