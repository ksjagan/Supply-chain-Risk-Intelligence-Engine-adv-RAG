# Shipment Incident INC-2026-0013

Incident ID: INC-2026-0013
Supplier: Vertex Cells Poland
Supplier ID: SUP-0058
Component: Connectivity Module Module 245
Component ID: CMP-0245
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 9
Delay Reason: port congestion
Escalation Level: amber

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as port congestion. The affected component is
Connectivity Module Module 245. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 27, Orion Smart Hub 55.
Single-source product-component mappings for this component: 1.
The incident can create line stoppage risk if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- review active shipments from the same origin port
- check high-revenue products using the affected component
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Vertex Cells Poland; component Connectivity Module Module 245; country Poland; port Gdansk; delay 9 days; reason port congestion; escalation amber.
