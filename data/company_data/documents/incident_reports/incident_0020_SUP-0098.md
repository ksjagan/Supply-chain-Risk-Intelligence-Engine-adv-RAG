# Shipment Incident INC-2026-0020

Incident ID: INC-2026-0020
Supplier: Shenzhen Optics Poland
Supplier ID: SUP-0098
Component: Connectivity Module Module 080
Component ID: CMP-0080
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 15
Delay Reason: geopolitical export controls
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as geopolitical export controls. The affected component is
Connectivity Module Module 080. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Helios Energy Controller 41, Zenith Edge Server 66.
Single-source product-component mappings for this component: 1.
The incident can create customer-service exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- ask planning to model a two-week supply interruption
- compare the issue against the last three supplier scorecards
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Shenzhen Optics Poland; component Connectivity Module Module 080; country Poland; port Gdansk; delay 15 days; reason geopolitical export controls; escalation red.
