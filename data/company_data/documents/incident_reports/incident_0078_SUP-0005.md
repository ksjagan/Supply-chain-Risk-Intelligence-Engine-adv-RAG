# Shipment Incident INC-2026-0078

Incident ID: INC-2026-0078
Supplier: Korea Electronics Mexico
Supplier ID: SUP-0005
Component: Battery Module 164
Component ID: CMP-0164
Origin Country: Mexico
Origin Port: Manzanillo
Delay Days: 19
Delay Reason: commodity price volatility
Escalation Level: red

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as commodity price volatility. The affected component is
Battery Module 164. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: Orion Smart Hub 13.
Single-source product-component mappings for this component: 1.
The incident can create revenue-at-risk exposure if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- review active shipments from the same origin port
- confirm open purchase orders due in the next 45 days
- Ask logistics to validate whether other shipments from Manzanillo have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier Korea Electronics Mexico; component Battery Module 164; country Mexico; port Manzanillo; delay 19 days; reason commodity price volatility; escalation red.
