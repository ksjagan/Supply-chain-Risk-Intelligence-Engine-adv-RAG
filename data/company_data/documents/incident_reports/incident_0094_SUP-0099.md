# Shipment Incident INC-2026-0094

Incident ID: INC-2026-0094
Supplier: Vertex Cells Vietnam
Supplier ID: SUP-0099
Component: Display Module Module 336
Component ID: CMP-0336
Origin Country: Vietnam
Origin Port: Cat Lai
Delay Days: 18
Delay Reason: customs inspection delays
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as customs inspection delays. The affected component is
Display Module Module 336. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Nova Health Monitor 47, Vega Retail Sensor 57, Vega Retail Sensor 58, Zenith Edge Server 03, Zenith Edge Server 66.
Single-source product-component mappings for this component: 0.
The incident can create regulatory hold risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- check high-revenue products using the affected component
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Cat Lai have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Vertex Cells Vietnam; component Display Module Module 336; country Vietnam; port Cat Lai; delay 18 days; reason customs inspection delays; escalation red.
