# Shipment Incident INC-2026-0008

Incident ID: INC-2026-0008
Supplier: Bharat Electronics Germany
Supplier ID: SUP-0119
Component: Power Electronics Module 051
Component ID: CMP-0051
Origin Country: Germany
Origin Port: Hamburg
Delay Days: 16
Delay Reason: port congestion
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Power Electronics Module 051. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Orion Smart Hub 55, Zenith Edge Server 20.
Single-source product-component mappings for this component: 0.
The incident can create premium freight exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- review active shipments from the same origin port
- ask planning to model a two-week supply interruption
- Ask logistics to validate whether other shipments from Hamburg have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Bharat Electronics Germany; component Power Electronics Module 051; country Germany; port Hamburg; delay 16 days; reason port congestion; escalation red.
