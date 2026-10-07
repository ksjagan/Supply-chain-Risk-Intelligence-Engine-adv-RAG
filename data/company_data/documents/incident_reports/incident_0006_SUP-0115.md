# Shipment Incident INC-2026-0006

Incident ID: INC-2026-0006
Supplier: Taiwan Assembly Germany
Supplier ID: SUP-0115
Component: Sensor Module 246
Component ID: CMP-0246
Origin Country: Germany
Origin Port: Hamburg
Delay Days: 22
Delay Reason: quality escape
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as quality escape. The affected component is
Sensor Module 246. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 14, Orion Smart Hub 09, Vega Retail Sensor 16.
Single-source product-component mappings for this component: 1.
The incident can create premium freight exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- check high-revenue products using the affected component
- Ask logistics to validate whether other shipments from Hamburg have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Taiwan Assembly Germany; component Sensor Module 246; country Germany; port Hamburg; delay 22 days; reason quality escape; escalation red.
