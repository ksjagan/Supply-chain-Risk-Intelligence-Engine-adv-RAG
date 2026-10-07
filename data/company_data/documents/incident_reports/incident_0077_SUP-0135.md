# Shipment Incident INC-2026-0077

Incident ID: INC-2026-0077
Supplier: Bharat MicroSystems Malaysia
Supplier ID: SUP-0135
Component: Sensor Module 278
Component ID: CMP-0278
Origin Country: Malaysia
Origin Port: Port Klang
Delay Days: 16
Delay Reason: capacity shortage
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as capacity shortage. The affected component is
Sensor Module 278. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 61, Atlas Robotics Kit 04.
Single-source product-component mappings for this component: 2.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Port Klang have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Bharat MicroSystems Malaysia; component Sensor Module 278; country Malaysia; port Port Klang; delay 16 days; reason capacity shortage; escalation red.
