# Shipment Incident INC-2026-0032

Incident ID: INC-2026-0032
Supplier: Delta Materials Vietnam
Supplier ID: SUP-0006
Component: Power Electronics Module 338
Component ID: CMP-0338
Origin Country: Vietnam
Origin Port: Cat Lai
Delay Days: 3
Delay Reason: labor disruption
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as labor disruption. The affected component is
Power Electronics Module 338. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Atlas Robotics Kit 74, Helios Energy Controller 53.
Single-source product-component mappings for this component: 2.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- review active shipments from the same origin port
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Cat Lai have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Delta Materials Vietnam; component Power Electronics Module 338; country Vietnam; port Cat Lai; delay 3 days; reason labor disruption; escalation watch.
