# Shipment Incident INC-2026-0048

Incident ID: INC-2026-0048
Supplier: Mekong Foundry Poland
Supplier ID: SUP-0112
Component: Semiconductor Module 357
Component ID: CMP-0357
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 11
Delay Reason: compliance documentation gap
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as compliance documentation gap. The affected component is
Semiconductor Module 357. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Pulse Wearable Dock 15, Vega Retail Sensor 70, Zenith Edge Server 17, Zenith Edge Server 20.
Single-source product-component mappings for this component: 2.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- compare the issue against the last three supplier scorecards
- validate whether alternate suppliers are production-qualified
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Mekong Foundry Poland; component Semiconductor Module 357; country Poland; port Gdansk; delay 11 days; reason compliance documentation gap; escalation amber.
