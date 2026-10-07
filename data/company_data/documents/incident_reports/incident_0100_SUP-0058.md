# Shipment Incident INC-2026-0100

Incident ID: INC-2026-0100
Supplier: Vertex Cells Poland
Supplier ID: SUP-0058
Component: Connectivity Module Module 400
Component ID: CMP-0400
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 11
Delay Reason: geopolitical export controls
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as geopolitical export controls. The affected component is
Connectivity Module Module 400. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Orion Smart Hub 22, Orion Smart Hub 40.
Single-source product-component mappings for this component: 2.
The incident can create customer-service exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- review active shipments from the same origin port
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Vertex Cells Poland; component Connectivity Module Module 400; country Poland; port Gdansk; delay 11 days; reason geopolitical export controls; escalation amber.
