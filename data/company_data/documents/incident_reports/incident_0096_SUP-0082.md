# Shipment Incident INC-2026-0096

Incident ID: INC-2026-0096
Supplier: Taiwan Electronics Poland
Supplier ID: SUP-0082
Component: Battery Module 191
Component ID: CMP-0191
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 5
Delay Reason: quality escape
Escalation Level: watch

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as quality escape. The affected component is
Battery Module 191. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 61, Pulse Wearable Dock 25, Pulse Wearable Dock 77.
Single-source product-component mappings for this component: 0.
The incident can create premium freight exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Taiwan Electronics Poland; component Battery Module 191; country Poland; port Gdansk; delay 5 days; reason quality escape; escalation watch.
