"""
Generate a realistic synthetic enterprise dataset for the Supply Chain Risk
Intelligence Engine.

The goal is not random filler data. The generator creates consistent suppliers,
components, products, shipments, incidents, compliance records, and risk reports
so retrieval can answer multi-hop business questions with grounded evidence.
"""

from __future__ import annotations

import csv
import json
import random
import shutil
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from pathlib import Path


RANDOM_SEED = 42
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "company_data"
TABLE_DIR = OUTPUT_DIR / "tables"
DOC_DIR = OUTPUT_DIR / "documents"
EVAL_DIR = OUTPUT_DIR / "eval"


COUNTRIES = [
    ("Malaysia", "APAC", "Port Klang"),
    ("Vietnam", "APAC", "Cat Lai"),
    ("China", "APAC", "Yantian"),
    ("Taiwan", "APAC", "Kaohsiung"),
    ("South Korea", "APAC", "Busan"),
    ("India", "APAC", "Nhava Sheva"),
    ("Mexico", "North America", "Manzanillo"),
    ("Poland", "Europe", "Gdansk"),
    ("Germany", "Europe", "Hamburg"),
    ("Turkey", "EMEA", "Mersin"),
]

CATEGORIES = [
    "semiconductor",
    "battery",
    "printed circuit board",
    "display module",
    "sensor",
    "mechanical housing",
    "power electronics",
    "connectivity module",
]

RISK_THEMES = [
    "port congestion",
    "customs inspection delays",
    "geopolitical export controls",
    "labor disruption",
    "quality escape",
    "commodity price volatility",
    "capacity shortage",
    "compliance documentation gap",
]

PRODUCT_FAMILIES = [
    "Orion Smart Hub",
    "Aster Industrial Gateway",
    "Nova Health Monitor",
    "Helios Energy Controller",
    "Vega Retail Sensor",
    "Atlas Robotics Kit",
    "Pulse Wearable Dock",
    "Zenith Edge Server",
]

SUPPLIER_PREFIXES = [
    "Nova",
    "Delta",
    "Apex",
    "Mekong",
    "Shenzhen",
    "Korea",
    "Taiwan",
    "Bharat",
    "Nordic",
    "Azura",
    "Vertex",
    "Summit",
]

SUPPLIER_SUFFIXES = [
    "MicroSystems",
    "Precision",
    "Circuits",
    "Cells",
    "Foundry",
    "Electronics",
    "Components",
    "Assembly",
    "Materials",
    "Optics",
]

OWNERS = [
    "Global Procurement",
    "Supplier Quality Engineering",
    "Logistics Control Tower",
    "Trade Compliance",
    "Manufacturing Planning",
    "Strategic Sourcing",
]

CONTROLS = [
    "weekly control-tower review",
    "expedited document refresh",
    "alternate-source validation",
    "safety-stock exception",
    "supplier corrective action plan",
    "executive escalation checkpoint",
]

IMPACT_LEVELS = [
    "line stoppage risk",
    "margin exposure",
    "customer-service exposure",
    "regulatory hold risk",
    "premium freight exposure",
    "revenue-at-risk exposure",
]

NEXT_ACTIONS = [
    "confirm open purchase orders due in the next 45 days",
    "validate whether alternate suppliers are production-qualified",
    "check high-revenue products using the affected component",
    "compare the issue against the last three supplier scorecards",
    "review active shipments from the same origin port",
    "ask planning to model a two-week supply interruption",
]


@dataclass
class Supplier:
    supplier_id: str
    supplier_name: str
    country: str
    region: str
    port: str
    category: str
    risk_tier: str
    on_time_rate: float
    compliance_score: int
    quality_score: int
    capacity_utilization: int


@dataclass
class Component:
    component_id: str
    component_name: str
    category: str
    criticality: str
    lifecycle_stage: str


@dataclass
class Product:
    product_id: str
    product_name: str
    business_unit: str
    annual_revenue_musd: int
    gross_margin_pct: int
    priority_level: str
    production_plant: str


def reset_output() -> None:
    """Remove previous generated data so every run is deterministic and clean."""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    for folder in [
        TABLE_DIR,
        EVAL_DIR,
        DOC_DIR / "supplier_profiles",
        DOC_DIR / "risk_reports",
        DOC_DIR / "incident_reports",
        DOC_DIR / "compliance_reports",
        DOC_DIR / "logistics_memos",
        DOC_DIR / "market_reports",
    ]:
        folder.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, rows: list[dict]) -> None:
    """Write a list of dictionaries as a CSV table."""
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, title: str, body: str) -> None:
    """Write a business document in Markdown for LangChain document loading."""
    path.write_text(f"# {title}\n\n{body.strip()}\n", encoding="utf-8")


def make_suppliers(count: int = 150) -> list[Supplier]:
    suppliers: list[Supplier] = []
    used_names: set[str] = set()
    for index in range(1, count + 1):
        country, region, port = random.choice(COUNTRIES)
        category = random.choice(CATEGORIES)
        name = f"{random.choice(SUPPLIER_PREFIXES)} {random.choice(SUPPLIER_SUFFIXES)} {country}"
        while name in used_names:
            name = f"{random.choice(SUPPLIER_PREFIXES)} {random.choice(SUPPLIER_SUFFIXES)} {country} {index}"
        used_names.add(name)
        on_time = round(random.uniform(0.68, 0.98), 3)
        compliance = random.randint(62, 99)
        quality = random.randint(65, 99)
        capacity = random.randint(58, 99)
        risk_tier = "High" if on_time < 0.78 or compliance < 72 or capacity > 92 else "Medium" if on_time < 0.88 or compliance < 84 else "Low"
        suppliers.append(
            Supplier(
                supplier_id=f"SUP-{index:04d}",
                supplier_name=name,
                country=country,
                region=region,
                port=port,
                category=category,
                risk_tier=risk_tier,
                on_time_rate=on_time,
                compliance_score=compliance,
                quality_score=quality,
                capacity_utilization=capacity,
            )
        )
    return suppliers


def make_components(count: int = 400) -> list[Component]:
    components: list[Component] = []
    for index in range(1, count + 1):
        category = random.choice(CATEGORIES)
        label = category.title().replace("Pcb", "PCB")
        components.append(
            Component(
                component_id=f"CMP-{index:04d}",
                component_name=f"{label} Module {index:03d}",
                category=category,
                criticality=random.choices(["critical", "high", "standard"], weights=[25, 35, 40])[0],
                lifecycle_stage=random.choice(["new", "growth", "mature", "end-of-life"]),
            )
        )
    return components


def make_products(count: int = 80) -> list[Product]:
    products: list[Product] = []
    for index in range(1, count + 1):
        family = random.choice(PRODUCT_FAMILIES)
        products.append(
            Product(
                product_id=f"PRD-{index:03d}",
                product_name=f"{family} {index:02d}",
                business_unit=random.choice(["Consumer IoT", "Industrial Systems", "Healthcare Devices", "Energy Automation"]),
                annual_revenue_musd=random.randint(35, 950),
                gross_margin_pct=random.randint(18, 61),
                priority_level=random.choices(["tier_1", "tier_2", "tier_3"], weights=[30, 45, 25])[0],
                production_plant=random.choice(["Austin Plant", "Pune Plant", "Wroclaw Plant", "Monterrey Plant"]),
            )
        )
    return products


def make_bom(products: list[Product], components: list[Component], suppliers: list[Supplier]) -> list[dict]:
    rows: list[dict] = []
    compatible = {}
    for component in components:
        candidates = [s for s in suppliers if s.category == component.category]
        compatible[component.component_id] = candidates or suppliers

    for product in products:
        selected_components = random.sample(components, random.randint(5, 9))
        for component in selected_components:
            supplier_pool = compatible[component.component_id]
            primary = random.choice(supplier_pool)
            alternate = random.choice(supplier_pool) if random.random() > 0.38 and len(supplier_pool) > 1 else None
            rows.append(
                {
                    "product_id": product.product_id,
                    "product_name": product.product_name,
                    "component_id": component.component_id,
                    "component_name": component.component_name,
                    "primary_supplier_id": primary.supplier_id,
                    "primary_supplier_name": primary.supplier_name,
                    "alternate_supplier_id": alternate.supplier_id if alternate else "",
                    "alternate_supplier_name": alternate.supplier_name if alternate else "",
                    "component_criticality": component.criticality,
                    "quantity_per_unit": random.randint(1, 12),
                    "single_source_flag": "yes" if alternate is None else "no",
                }
            )
    return rows


def make_shipments(bom_rows: list[dict], suppliers_by_id: dict[str, Supplier], count: int = 2500) -> list[dict]:
    rows: list[dict] = []
    start = date(2026, 1, 1)
    for index in range(1, count + 1):
        bom = random.choice(bom_rows)
        supplier = suppliers_by_id[bom["primary_supplier_id"]]
        planned_departure = start + timedelta(days=random.randint(0, 250))
        planned_arrival = planned_departure + timedelta(days=random.randint(8, 38))
        delay_probability = 0.14 if supplier.risk_tier == "Low" else 0.26 if supplier.risk_tier == "Medium" else 0.42
        delayed = random.random() < delay_probability
        delay_days = random.randint(3, 24) if delayed else 0
        reason = random.choice(RISK_THEMES) if delayed else ""
        rows.append(
            {
                "shipment_id": f"SHP-{index:05d}",
                "supplier_id": supplier.supplier_id,
                "supplier_name": supplier.supplier_name,
                "origin_country": supplier.country,
                "origin_port": supplier.port,
                "destination_plant": random.choice(["Austin Plant", "Pune Plant", "Wroclaw Plant", "Monterrey Plant"]),
                "component_id": bom["component_id"],
                "component_name": bom["component_name"],
                "planned_departure": planned_departure.isoformat(),
                "actual_departure": (planned_departure + timedelta(days=max(0, delay_days - 2))).isoformat() if delayed else planned_departure.isoformat(),
                "planned_arrival": planned_arrival.isoformat(),
                "actual_arrival": (planned_arrival + timedelta(days=delay_days)).isoformat() if delayed else planned_arrival.isoformat(),
                "status": "delayed" if delayed else random.choice(["in_transit", "delivered", "booked"]),
                "delay_days": delay_days,
                "delay_reason": reason,
                "carrier": random.choice(["Maersk", "MSC", "DHL Global", "FedEx Trade", "Kuehne+Nagel"]),
                "risk_flag": "yes" if delayed and delay_days >= 7 else "no",
            }
        )
    return rows


def make_purchase_orders(bom_rows: list[dict], suppliers_by_id: dict[str, Supplier], count: int = 1500) -> list[dict]:
    rows: list[dict] = []
    start = date(2026, 1, 1)
    for index in range(1, count + 1):
        bom = random.choice(bom_rows)
        supplier = suppliers_by_id[bom["primary_supplier_id"]]
        order_date = start + timedelta(days=random.randint(0, 230))
        expected = order_date + timedelta(days=random.randint(20, 70))
        late = random.random() > supplier.on_time_rate
        rows.append(
            {
                "po_id": f"PO-{index:05d}",
                "supplier_id": supplier.supplier_id,
                "supplier_name": supplier.supplier_name,
                "component_id": bom["component_id"],
                "component_name": bom["component_name"],
                "quantity": random.randint(500, 60000),
                "unit_cost_usd": round(random.uniform(0.8, 180.0), 2),
                "order_date": order_date.isoformat(),
                "expected_delivery_date": expected.isoformat(),
                "actual_delivery_date": (expected + timedelta(days=random.randint(2, 18))).isoformat() if late else expected.isoformat(),
                "plant": random.choice(["Austin Plant", "Pune Plant", "Wroclaw Plant", "Monterrey Plant"]),
                "status": "late" if late else random.choice(["received", "open", "closed"]),
            }
        )
    return rows


def make_scorecards(suppliers: list[Supplier]) -> list[dict]:
    rows: list[dict] = []
    months = [date(2026, month, 1).isoformat() for month in range(1, 9)]
    for supplier in suppliers:
        for month in months:
            rows.append(
                {
                    "supplier_id": supplier.supplier_id,
                    "supplier_name": supplier.supplier_name,
                    "month": month,
                    "on_time_delivery_rate": round(max(0.45, min(0.99, supplier.on_time_rate + random.uniform(-0.06, 0.04))), 3),
                    "defect_rate_pct": round(random.uniform(0.2, 6.5) + (2.5 if supplier.quality_score < 75 else 0), 2),
                    "quality_score": max(45, min(100, supplier.quality_score + random.randint(-5, 4))),
                    "responsiveness_score": random.randint(55, 98),
                    "compliance_score": max(45, min(100, supplier.compliance_score + random.randint(-4, 3))),
                    "capacity_utilization": max(40, min(100, supplier.capacity_utilization + random.randint(-6, 5))),
                    "risk_tier": supplier.risk_tier,
                }
            )
    return rows


def document_safe_name(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "_" for ch in value).strip("_")


def make_documents(
    suppliers: list[Supplier],
    products: list[Product],
    bom_rows: list[dict],
    shipments: list[dict],
) -> None:
    bom_by_supplier: dict[str, list[dict]] = {}
    for row in bom_rows:
        bom_by_supplier.setdefault(row["primary_supplier_id"], []).append(row)

    shipment_by_supplier: dict[str, list[dict]] = {}
    for row in shipments:
        shipment_by_supplier.setdefault(row["supplier_id"], []).append(row)

    for supplier in suppliers:
        linked_bom = bom_by_supplier.get(supplier.supplier_id, [])
        components = sorted({row["component_name"] for row in linked_bom})[:6]
        products_linked = sorted({row["product_name"] for row in linked_bom})[:6]
        delayed = [row for row in shipment_by_supplier.get(supplier.supplier_id, []) if row["status"] == "delayed"]
        single_source_count = sum(1 for row in linked_bom if row["single_source_flag"] == "yes")
        owner = random.choice(OWNERS)
        control = random.choice(CONTROLS)
        action = random.choice(NEXT_ACTIONS)
        impact = random.choice(IMPACT_LEVELS)
        body = f"""
Supplier ID: {supplier.supplier_id}
Supplier Name: {supplier.supplier_name}
Country: {supplier.country}
Region: {supplier.region}
Primary Port: {supplier.port}
Category: {supplier.category}
Risk Tier: {supplier.risk_tier}

{supplier.supplier_name} supplies {supplier.category} parts for enterprise hardware product lines.
The supplier's current on-time delivery rate is {supplier.on_time_rate}, compliance score is {supplier.compliance_score},
quality score is {supplier.quality_score}, and capacity utilization is {supplier.capacity_utilization}%.

## Commercial and Operational Context

This supplier is managed by {owner}. The current commercial posture is {supplier.risk_tier.lower()} risk because the operating profile combines delivery reliability, compliance evidence, quality trend, and capacity headroom. The most relevant business exposure is {impact}, especially when production planners do not have confirmed alternate supply.

Important supplied components include: {", ".join(components) if components else "no active mapped components"}.
Affected products include: {", ".join(products_linked) if products_linked else "no active mapped products"}.
Mapped BOM relationships: {len(linked_bom)}.
Single-source BOM relationships: {single_source_count}.

Recent shipment review found {len(delayed)} delayed shipments. The most common operational concern is
{random.choice(RISK_THEMES)}. Procurement should monitor supplier concentration and alternate source coverage.

## Control Plan

- Primary control: {control}
- Required next action: {action}
- Planning note: prioritize tier_1 products, components marked critical, and open orders due inside the next two production cycles.
- Analyst note: this profile should be retrieved for questions about {supplier.country}, {supplier.category}, supplier concentration, single-source risk, shipment delays, or compliance weakness.
"""
        write_markdown(
            DOC_DIR / "supplier_profiles" / f"supplier_profile_{supplier.supplier_id}_{document_safe_name(supplier.supplier_name)}.md",
            f"Supplier Profile - {supplier.supplier_name}",
            body,
        )

    for index, shipment in enumerate([s for s in shipments if s["status"] == "delayed"][:100], start=1):
        linked_products = sorted({row["product_name"] for row in bom_rows if row["component_id"] == shipment["component_id"]})[:6]
        single_source_rows = sum(1 for row in bom_rows if row["component_id"] == shipment["component_id"] and row["single_source_flag"] == "yes")
        escalation = "red" if int(shipment["delay_days"]) >= 14 else "amber" if int(shipment["delay_days"]) >= 8 else "watch"
        body = f"""
Incident ID: INC-2026-{index:04d}
Supplier: {shipment["supplier_name"]}
Supplier ID: {shipment["supplier_id"]}
Component: {shipment["component_name"]}
Component ID: {shipment["component_id"]}
Origin Country: {shipment["origin_country"]}
Origin Port: {shipment["origin_port"]}
Delay Days: {shipment["delay_days"]}
Delay Reason: {shipment["delay_reason"]}
Escalation Level: {escalation}

The shipment was flagged because actual arrival moved beyond the planned arrival date.
The delay reason was recorded as {shipment["delay_reason"]}. The affected component is
{shipment["component_name"]}. Operations should check finished products that depend on this component,
especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: {", ".join(linked_products) if linked_products else "no linked product found"}.
Single-source product-component mappings for this component: {single_source_rows}.
The incident can create {random.choice(IMPACT_LEVELS)} if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- {random.choice(NEXT_ACTIONS)}
- {random.choice(NEXT_ACTIONS)}
- Ask logistics to validate whether other shipments from {shipment["origin_port"]} have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier {shipment["supplier_name"]}; component {shipment["component_name"]}; country {shipment["origin_country"]}; port {shipment["origin_port"]}; delay {shipment["delay_days"]} days; reason {shipment["delay_reason"]}; escalation {escalation}.
"""
        write_markdown(DOC_DIR / "incident_reports" / f"incident_{index:04d}_{shipment['supplier_id']}.md", f"Shipment Incident INC-2026-{index:04d}", body)

    for index in range(1, 121):
        country, region, port = random.choice(COUNTRIES)
        category = random.choice(CATEGORIES)
        theme = random.choice(RISK_THEMES)
        severity = random.choice(["elevated", "moderate", "severe"])
        body = f"""
Report ID: RISK-2026-{index:04d}
Region: {region}
Country: {country}
Port: {port}
Category: {category}
Risk Theme: {theme}
Severity: {severity}

The current risk outlook for {category} supply from {country} is {severity}. Analysts cite
{theme} as the primary driver. Suppliers shipping through {port} may experience variability in
transit time, customs release, and production scheduling.

## Analyst Assessment

Risk is most material for suppliers with high capacity utilization, low on-time delivery, or components that map to single-source BOM rows. The practical signal to monitor is whether shipment delays, supplier scorecard deterioration, and compliance exceptions appear together for the same supplier or category.

## Exposure Pattern

- Region affected: {region}
- Country affected: {country}
- Port dependency: {port}
- Component category: {category}
- Primary risk driver: {theme}
- Severity call: {severity}

## Recommended Actions

- Increase safety stock for critical {category} components.
- Validate alternate supplier readiness for products with high revenue contribution.
- Review shipments from {port} with delay risk flags.
- Prioritize high-revenue products with single-source exposure.
- Recheck procurement contracts for premium freight and recovery clauses.
"""
        write_markdown(DOC_DIR / "risk_reports" / f"risk_report_{index:04d}_{document_safe_name(country)}_{document_safe_name(category)}.md", f"Risk Report - {country} {category}", body)

    high_or_medium = [s for s in suppliers if s.risk_tier in {"High", "Medium"}]
    for index, supplier in enumerate(random.sample(high_or_medium, min(70, len(high_or_medium))), start=1):
        finding = random.choice(["missing audit refresh", "expired ISO certificate", "restricted-party screening hit", "incomplete ESG evidence"])
        severity = "high" if supplier.compliance_score < 70 else "medium" if supplier.compliance_score < 82 else "watch"
        control = random.choice(CONTROLS)
        owner = random.choice(OWNERS)
        linked_bom = bom_by_supplier.get(supplier.supplier_id, [])
        products_linked = sorted({row["product_name"] for row in linked_bom})[:6]
        single_source_count = sum(1 for row in linked_bom if row["single_source_flag"] == "yes")
        body = f"""
Compliance Review ID: COMP-2026-{index:04d}
Supplier: {supplier.supplier_name}
Supplier ID: {supplier.supplier_id}
Country: {supplier.country}
Category: {supplier.category}
Compliance Score: {supplier.compliance_score}
Finding: {finding}
Severity: {severity}
Control Owner: {owner}

The compliance team reviewed documentation for {supplier.supplier_name}. The main finding was
{finding}. This does not automatically block purchasing, but it increases supplier risk when paired
with late shipments, poor quality trends, or lack of alternate suppliers.

## Evidence Reviewed

- Supplier master profile for {supplier.supplier_name}
- Contract and certification packet for {supplier.category}
- Recent supplier scorecard trend
- Restricted-party and ESG documentation status
- Open BOM exposure for products using this supplier

## Business Exposure

Mapped products: {", ".join(products_linked) if products_linked else "no mapped products"}.
Mapped BOM rows: {len(linked_bom)}.
Single-source BOM rows: {single_source_count}.
Primary business concern: {random.choice(IMPACT_LEVELS)}.

If this compliance issue remains open, procurement should avoid increasing allocation until the evidence packet is refreshed. The risk is more serious when the supplier also has delayed shipments, low quality score, high capacity utilization, or no approved alternate supplier.

## Required Mitigation

- Control: {control}
- Action: {random.choice(NEXT_ACTIONS)}
- Escalation rule: escalate to supplier risk council if the finding is not closed before the next purchase-order release.
- Analyst note: retrieve this document for questions about compliance risk, audit gaps, supplier screening, ESG evidence, alternate sourcing, or supplier concentration.
"""
        write_markdown(DOC_DIR / "compliance_reports" / f"compliance_{index:04d}_{supplier.supplier_id}.md", f"Compliance Review - {supplier.supplier_name}", body)

    for index in range(1, 41):
        country, region, port = random.choice(COUNTRIES)
        congestion = random.choice(["low", "moderate", "high", "critical"])
        body = f"""
Logistics Memo ID: LOG-2026-{index:04d}
Port: {port}
Country: {country}
Region: {region}
Congestion Level: {congestion}

The logistics control tower reports {congestion} congestion at {port}. Shipments from this port
should be reviewed for components used in tier_1 products and for suppliers with high capacity
utilization. Delays can cascade into production risk when there is single-source component coverage.

## Control-Tower Notes

The port risk is most important for shipments with near-term production demand, premium freight exposure, or components used by multiple finished products. The control tower recommends comparing all delayed shipments from {port} against BOM rows where single_source_flag is yes.

## Response Guidance

- Review supplier scorecards for origin-country suppliers.
- Check shipments with risk_flag yes and delay_days greater than seven.
- Ask planning to identify products with less than two weeks of component coverage.
- Use alternate carriers only for tier_1 products or customer-critical orders.

## Search Keywords

{port}; {country}; {region}; congestion {congestion}; shipment delay; logistics risk; single-source component; product exposure.
"""
        write_markdown(DOC_DIR / "logistics_memos" / f"logistics_memo_{index:04d}_{document_safe_name(port)}.md", f"Logistics Memo - {port}", body)

    for index in range(1, 61):
        category = random.choice(CATEGORIES)
        movement = random.choice(["rising prices", "tight capacity", "softening demand", "allocation pressure"])
        body = f"""
Market Report ID: MKT-2026-{index:04d}
Category: {category}
Market Signal: {movement}

Market intelligence indicates {movement} for {category}. Procurement should evaluate contract coverage,
supplier concentration, and exposure to high-margin products. The risk is highest where critical components
have no approved alternate supplier and shipment lead times are already increasing.

## Procurement Implications

The category team should review supplier concentration, open purchase orders, and BOM criticality before negotiating the next allocation cycle. {category} risk can become product revenue risk when demand is firm but supply recovery requires qualification lead time.

## Recommended Actions

- Identify critical and high components in this category.
- Review products with annual revenue above 250M USD that depend on those components.
- Check whether alternate suppliers are approved and production-ready.
- Add contract clauses for expedite support, allocation transparency, and quality containment.

## Evidence Keywords

category {category}; market signal {movement}; supplier concentration; high-margin products; alternate supplier; BOM criticality; lead time risk.
"""
        write_markdown(DOC_DIR / "market_reports" / f"market_report_{index:04d}_{document_safe_name(category)}.md", f"Market Report - {category}", body)


def make_eval_questions(suppliers: list[Supplier], bom_rows: list[dict], shipments: list[dict]) -> list[dict]:
    questions: list[dict] = []
    delayed = [row for row in shipments if row["status"] == "delayed" and row["delay_days"] >= 7]
    for index, shipment in enumerate(delayed[:30], start=1):
        linked_products = sorted({row["product_name"] for row in bom_rows if row["component_id"] == shipment["component_id"]})
        questions.append(
            {
                "question_id": f"EVAL-{index:03d}",
                "question": f"Which products are exposed to {shipment['component_name']} delays from {shipment['supplier_name']}?",
                "strategy_type": "multi_hop",
                "expected_entities": [shipment["supplier_name"], shipment["component_name"], *linked_products[:3]],
                "ideal_answer_points": [
                    "identify delayed supplier",
                    "identify affected component",
                    "map component to products",
                    "mention delay evidence",
                ],
            }
        )

    high_risk = [s for s in suppliers if s.risk_tier == "High"]
    for offset, supplier in enumerate(high_risk[:30], start=31):
        questions.append(
            {
                "question_id": f"EVAL-{offset:03d}",
                "question": f"What risks should procurement monitor for {supplier.supplier_name}?",
                "strategy_type": "hybrid_rerank",
                "expected_entities": [supplier.supplier_name, supplier.country, supplier.category],
                "ideal_answer_points": [
                    "supplier risk tier",
                    "country or port exposure",
                    "delivery or compliance signal",
                    "recommended mitigation",
                ],
            }
        )
    return questions


def main() -> None:
    random.seed(RANDOM_SEED)
    reset_output()

    suppliers = make_suppliers()
    components = make_components()
    products = make_products()
    suppliers_by_id = {supplier.supplier_id: supplier for supplier in suppliers}
    bom_rows = make_bom(products, components, suppliers)
    shipments = make_shipments(bom_rows, suppliers_by_id)
    purchase_orders = make_purchase_orders(bom_rows, suppliers_by_id)
    scorecards = make_scorecards(suppliers)

    write_csv(TABLE_DIR / "suppliers.csv", [asdict(s) for s in suppliers])
    write_csv(TABLE_DIR / "components.csv", [asdict(c) for c in components])
    write_csv(TABLE_DIR / "products.csv", [asdict(p) for p in products])
    write_csv(TABLE_DIR / "bill_of_materials.csv", bom_rows)
    write_csv(TABLE_DIR / "shipments.csv", shipments)
    write_csv(TABLE_DIR / "purchase_orders.csv", purchase_orders)
    write_csv(TABLE_DIR / "supplier_scorecards.csv", scorecards)

    make_documents(suppliers, products, bom_rows, shipments)
    eval_questions = make_eval_questions(suppliers, bom_rows, shipments)
    (EVAL_DIR / "eval_questions.json").write_text(json.dumps(eval_questions, indent=2), encoding="utf-8")

    manifest = {
        "suppliers": len(suppliers),
        "components": len(components),
        "products": len(products),
        "bom_rows": len(bom_rows),
        "shipments": len(shipments),
        "purchase_orders": len(purchase_orders),
        "scorecard_rows": len(scorecards),
        "documents": len(list(DOC_DIR.rglob("*.md"))),
        "eval_questions": len(eval_questions),
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
