# Shipment Incident INC-2026-0005

Incident ID: INC-2026-0005
Supplier: Nova Precision Poland
Supplier ID: SUP-0088
Component: Connectivity Module Module 055
Component ID: CMP-0055
Origin Country: Poland
Origin Port: Gdansk
Delay Days: 20
Delay Reason: labor disruption
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as labor disruption. The affected component is
Connectivity Module Module 055. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Aster Industrial Gateway 19, Vega Retail Sensor 45, Zenith Edge Server 06.
Single-source product-component mappings for this component: 1.
The incident can create margin exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- validate whether alternate suppliers are production-qualified
- confirm open purchase orders due in the next 45 days
- Ask logistics to validate whether other shipments from Gdansk have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Nova Precision Poland; component Connectivity Module Module 055; country Poland; port Gdansk; delay 20 days; reason labor disruption; escalation red.
