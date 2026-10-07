# Shipment Incident INC-2026-0084

Incident ID: INC-2026-0084
Supplier: Azura MicroSystems Poland
Supplier ID: SUP-0105
Component: Battery Module 281
Component ID: CMP-0281
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 24
Delay Reason: commodity price volatility
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as commodity price volatility. The affected component is
Battery Module 281. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Pulse Wearable Dock 29, Vega Retail Sensor 30.
Single-source product-component mappings for this component: 1.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- compare the issue against the last three supplier scorecards
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Azura MicroSystems Poland; component Battery Module 281; country Poland; port Gdansk; delay 24 days; reason commodity price volatility; escalation red.
