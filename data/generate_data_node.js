const fs = require("fs");
const path = require("path");

let seed = 42;
function random() {
  seed = (seed * 1664525 + 1013904223) % 4294967296;
  return seed / 4294967296;
}

function choice(items) {
  return items[Math.floor(random() * items.length)];
}

function sample(items, count) {
  const copy = [...items];
  const out = [];
  while (out.length < count && copy.length) {
    out.push(copy.splice(Math.floor(random() * copy.length), 1)[0]);
  }
  return out;
}

function randint(min, max) {
  return Math.floor(random() * (max - min + 1)) + min;
}

function safeName(value) {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_+|_+$/g, "");
}

function ensureDir(folder) {
  fs.mkdirSync(folder, { recursive: true });
}

function writeCsv(filePath, rows) {
  const headers = Object.keys(rows[0]);
  const lines = [headers.join(",")];
  for (const row of rows) {
    lines.push(headers.map((h) => `"${String(row[h] ?? "").replaceAll('"', '""')}"`).join(","));
  }
  fs.writeFileSync(filePath, lines.join("\n"), "utf8");
}

function writeMarkdown(filePath, title, body) {
  fs.writeFileSync(filePath, `# ${title}\n\n${body.trim()}\n`, "utf8");
}

function addDays(base, days) {
  const date = new Date(base);
  date.setUTCDate(date.getUTCDate() + days);
  return date.toISOString().slice(0, 10);
}

const root = path.resolve(__dirname, "company_data");
const tablesDir = path.join(root, "tables");
const docsDir = path.join(root, "documents");
const evalDir = path.join(root, "eval");

fs.rmSync(root, { recursive: true, force: true });
for (const folder of [
  tablesDir,
  evalDir,
  path.join(docsDir, "supplier_profiles"),
  path.join(docsDir, "risk_reports"),
  path.join(docsDir, "incident_reports"),
  path.join(docsDir, "compliance_reports"),
  path.join(docsDir, "logistics_memos"),
  path.join(docsDir, "market_reports"),
]) ensureDir(folder);

const countries = [
  ["Malaysia", "APAC", "Port Klang"],
  ["Vietnam", "APAC", "Cat Lai"],
  ["China", "APAC", "Yantian"],
  ["Taiwan", "APAC", "Kaohsiung"],
  ["South Korea", "APAC", "Busan"],
  ["India", "APAC", "Nhava Sheva"],
  ["Mexico", "North America", "Manzanillo"],
  ["Poland", "Europe", "Gdansk"],
  ["Germany", "Europe", "Hamburg"],
  ["Turkey", "EMEA", "Mersin"],
];
const categories = ["semiconductor", "battery", "printed circuit board", "display module", "sensor", "mechanical housing", "power electronics", "connectivity module"];
const riskThemes = ["port congestion", "customs inspection delays", "geopolitical export controls", "labor disruption", "quality escape", "commodity price volatility", "capacity shortage", "compliance documentation gap"];
const productFamilies = ["Orion Smart Hub", "Aster Industrial Gateway", "Nova Health Monitor", "Helios Energy Controller", "Vega Retail Sensor", "Atlas Robotics Kit", "Pulse Wearable Dock", "Zenith Edge Server"];
const prefixes = ["Nova", "Delta", "Apex", "Mekong", "Shenzhen", "Korea", "Taiwan", "Bharat", "Nordic", "Azura", "Vertex", "Summit"];
const suffixes = ["MicroSystems", "Precision", "Circuits", "Cells", "Foundry", "Electronics", "Components", "Assembly", "Materials", "Optics"];
const owners = ["Global Procurement", "Supplier Quality Engineering", "Logistics Control Tower", "Trade Compliance", "Manufacturing Planning", "Strategic Sourcing"];
const controls = ["weekly control-tower review", "expedited document refresh", "alternate-source validation", "safety-stock exception", "supplier corrective action plan", "executive escalation checkpoint"];
const impactLevels = ["line stoppage risk", "margin exposure", "customer-service exposure", "regulatory hold risk", "premium freight exposure", "revenue-at-risk exposure"];
const nextActions = [
  "confirm open purchase orders due in the next 45 days",
  "validate whether alternate suppliers are production-qualified",
  "check high-revenue products using the affected component",
  "compare the issue against the last three supplier scorecards",
  "review active shipments from the same origin port",
  "ask planning to model a two-week supply interruption",
];

const suppliers = [];
for (let i = 1; i <= 150; i++) {
  const [country, region, port] = choice(countries);
  const category = choice(categories);
  const onTime = Number((0.68 + random() * 0.3).toFixed(3));
  const compliance = randint(62, 99);
  const quality = randint(65, 99);
  const capacity = randint(58, 99);
  const riskTier = onTime < 0.78 || compliance < 72 || capacity > 92 ? "High" : onTime < 0.88 || compliance < 84 ? "Medium" : "Low";
  suppliers.push({
    supplier_id: `SUP-${String(i).padStart(4, "0")}`,
    supplier_name: `${choice(prefixes)} ${choice(suffixes)} ${country} ${i}`,
    country, region, port, category,
    risk_tier: riskTier,
    on_time_rate: onTime,
    compliance_score: compliance,
    quality_score: quality,
    capacity_utilization: capacity,
  });
}

const components = [];
for (let i = 1; i <= 400; i++) {
  const category = choice(categories);
  components.push({
    component_id: `CMP-${String(i).padStart(4, "0")}`,
    component_name: `${category.replace(/\b\w/g, (c) => c.toUpperCase())} Module ${String(i).padStart(3, "0")}`,
    category,
    criticality: choice(["critical", "high", "standard"]),
    lifecycle_stage: choice(["new", "growth", "mature", "end-of-life"]),
  });
}

const products = [];
for (let i = 1; i <= 80; i++) {
  products.push({
    product_id: `PRD-${String(i).padStart(3, "0")}`,
    product_name: `${choice(productFamilies)} ${String(i).padStart(2, "0")}`,
    business_unit: choice(["Consumer IoT", "Industrial Systems", "Healthcare Devices", "Energy Automation"]),
    annual_revenue_musd: randint(35, 950),
    gross_margin_pct: randint(18, 61),
    priority_level: choice(["tier_1", "tier_2", "tier_3"]),
    production_plant: choice(["Austin Plant", "Pune Plant", "Wroclaw Plant", "Monterrey Plant"]),
  });
}

const suppliersByCategory = {};
for (const supplier of suppliers) {
  suppliersByCategory[supplier.category] = suppliersByCategory[supplier.category] || [];
  suppliersByCategory[supplier.category].push(supplier);
}

const bom = [];
for (const product of products) {
  for (const component of sample(components, randint(5, 9))) {
    const pool = suppliersByCategory[component.category] || suppliers;
    const primary = choice(pool);
    const alternate = random() > 0.38 ? choice(pool) : null;
    bom.push({
      product_id: product.product_id,
      product_name: product.product_name,
      component_id: component.component_id,
      component_name: component.component_name,
      primary_supplier_id: primary.supplier_id,
      primary_supplier_name: primary.supplier_name,
      alternate_supplier_id: alternate ? alternate.supplier_id : "",
      alternate_supplier_name: alternate ? alternate.supplier_name : "",
      component_criticality: component.criticality,
      quantity_per_unit: randint(1, 12),
      single_source_flag: alternate ? "no" : "yes",
    });
  }
}

const supplierMap = Object.fromEntries(suppliers.map((s) => [s.supplier_id, s]));
const shipments = [];
for (let i = 1; i <= 2500; i++) {
  const row = choice(bom);
  const supplier = supplierMap[row.primary_supplier_id];
  const plannedDeparture = randint(0, 250);
  const plannedArrival = plannedDeparture + randint(8, 38);
  const delayProb = supplier.risk_tier === "Low" ? 0.14 : supplier.risk_tier === "Medium" ? 0.26 : 0.42;
  const delayed = random() < delayProb;
  const delayDays = delayed ? randint(3, 24) : 0;
  shipments.push({
    shipment_id: `SHP-${String(i).padStart(5, "0")}`,
    supplier_id: supplier.supplier_id,
    supplier_name: supplier.supplier_name,
    origin_country: supplier.country,
    origin_port: supplier.port,
    destination_plant: choice(["Austin Plant", "Pune Plant", "Wroclaw Plant", "Monterrey Plant"]),
    component_id: row.component_id,
    component_name: row.component_name,
    planned_departure: addDays("2026-01-01", plannedDeparture),
    actual_departure: addDays("2026-01-01", plannedDeparture + Math.max(0, delayDays - 2)),
    planned_arrival: addDays("2026-01-01", plannedArrival),
    actual_arrival: addDays("2026-01-01", plannedArrival + delayDays),
    status: delayed ? "delayed" : choice(["in_transit", "delivered", "booked"]),
    delay_days: delayDays,
    delay_reason: delayed ? choice(riskThemes) : "",
    carrier: choice(["Maersk", "MSC", "DHL Global", "FedEx Trade", "Kuehne+Nagel"]),
    risk_flag: delayed && delayDays >= 7 ? "yes" : "no",
  });
}

const purchaseOrders = [];
for (let i = 1; i <= 1500; i++) {
  const row = choice(bom);
  const supplier = supplierMap[row.primary_supplier_id];
  const orderOffset = randint(0, 230);
  const expectedOffset = orderOffset + randint(20, 70);
  const late = random() > supplier.on_time_rate;
  purchaseOrders.push({
    po_id: `PO-${String(i).padStart(5, "0")}`,
    supplier_id: supplier.supplier_id,
    supplier_name: supplier.supplier_name,
    component_id: row.component_id,
    component_name: row.component_name,
    quantity: randint(500, 60000),
    unit_cost_usd: Number((0.8 + random() * 179.2).toFixed(2)),
    order_date: addDays("2026-01-01", orderOffset),
    expected_delivery_date: addDays("2026-01-01", expectedOffset),
    actual_delivery_date: addDays("2026-01-01", expectedOffset + (late ? randint(2, 18) : 0)),
    plant: choice(["Austin Plant", "Pune Plant", "Wroclaw Plant", "Monterrey Plant"]),
    status: late ? "late" : choice(["received", "open", "closed"]),
  });
}

const scorecards = [];
for (const supplier of suppliers) {
  for (let month = 1; month <= 8; month++) {
    scorecards.push({
      supplier_id: supplier.supplier_id,
      supplier_name: supplier.supplier_name,
      month: `2026-${String(month).padStart(2, "0")}-01`,
      on_time_delivery_rate: Number(Math.max(0.45, Math.min(0.99, supplier.on_time_rate + random() * 0.1 - 0.06)).toFixed(3)),
      defect_rate_pct: Number((0.2 + random() * 6.3 + (supplier.quality_score < 75 ? 2.5 : 0)).toFixed(2)),
      quality_score: Math.max(45, Math.min(100, supplier.quality_score + randint(-5, 4))),
      responsiveness_score: randint(55, 98),
      compliance_score: Math.max(45, Math.min(100, supplier.compliance_score + randint(-4, 3))),
      capacity_utilization: Math.max(40, Math.min(100, supplier.capacity_utilization + randint(-6, 5))),
      risk_tier: supplier.risk_tier,
    });
  }
}

writeCsv(path.join(tablesDir, "suppliers.csv"), suppliers);
writeCsv(path.join(tablesDir, "components.csv"), components);
writeCsv(path.join(tablesDir, "products.csv"), products);
writeCsv(path.join(tablesDir, "bill_of_materials.csv"), bom);
writeCsv(path.join(tablesDir, "shipments.csv"), shipments);
writeCsv(path.join(tablesDir, "purchase_orders.csv"), purchaseOrders);
writeCsv(path.join(tablesDir, "supplier_scorecards.csv"), scorecards);

const bomBySupplier = {};
for (const row of bom) {
  bomBySupplier[row.primary_supplier_id] = bomBySupplier[row.primary_supplier_id] || [];
  bomBySupplier[row.primary_supplier_id].push(row);
}

const shipmentsBySupplier = {};
for (const shipment of shipments) {
  shipmentsBySupplier[shipment.supplier_id] = shipmentsBySupplier[shipment.supplier_id] || [];
  shipmentsBySupplier[shipment.supplier_id].push(shipment);
}

for (const supplier of suppliers) {
  const linkedBom = bomBySupplier[supplier.supplier_id] || [];
  const delayed = (shipmentsBySupplier[supplier.supplier_id] || []).filter((s) => s.status === "delayed");
  const componentsList = [...new Set(linkedBom.map((r) => r.component_name))].slice(0, 6).join(", ") || "no active mapped components";
  const productsList = [...new Set(linkedBom.map((r) => r.product_name))].slice(0, 6).join(", ") || "no active mapped products";
  const singleSourceCount = linkedBom.filter((r) => r.single_source_flag === "yes").length;
  const owner = choice(owners);
  const control = choice(controls);
  const action = choice(nextActions);
  const impact = choice(impactLevels);
  writeMarkdown(
    path.join(docsDir, "supplier_profiles", `supplier_profile_${supplier.supplier_id}_${safeName(supplier.supplier_name)}.md`),
    `Supplier Profile - ${supplier.supplier_name}`,
    `Supplier ID: ${supplier.supplier_id}
Supplier Name: ${supplier.supplier_name}
Country: ${supplier.country}
Region: ${supplier.region}
Primary Port: ${supplier.port}
Category: ${supplier.category}
Risk Tier: ${supplier.risk_tier}

${supplier.supplier_name} supplies ${supplier.category} parts for enterprise hardware product lines.
The supplier's current on-time delivery rate is ${supplier.on_time_rate}, compliance score is ${supplier.compliance_score},
quality score is ${supplier.quality_score}, and capacity utilization is ${supplier.capacity_utilization}%.

## Commercial and Operational Context

This supplier is managed by ${owner}. The current commercial posture is ${supplier.risk_tier.toLowerCase()} risk because the operating profile combines delivery reliability, compliance evidence, quality trend, and capacity headroom. The most relevant business exposure is ${impact}, especially when production planners do not have confirmed alternate supply.

Important supplied components include: ${componentsList}.
Affected products include: ${productsList}.
Mapped BOM relationships: ${linkedBom.length}.
Single-source BOM relationships: ${singleSourceCount}.

Recent shipment review found ${delayed.length} delayed shipments. The most common operational concern is ${choice(riskThemes)}.
Procurement should monitor supplier concentration and alternate source coverage.

## Control Plan

- Primary control: ${control}
- Required next action: ${action}
- Planning note: prioritize tier_1 products, components marked critical, and open orders due inside the next two production cycles.
- Analyst note: this profile should be retrieved for questions about ${supplier.country}, ${supplier.category}, supplier concentration, single-source risk, shipment delays, or compliance weakness.`
  );
}

const delayedShipments = shipments.filter((s) => s.status === "delayed");
for (let i = 0; i < Math.min(100, delayedShipments.length); i++) {
  const shipment = delayedShipments[i];
  const linkedProducts = [...new Set(bom.filter((r) => r.component_id === shipment.component_id).map((r) => r.product_name))].slice(0, 6);
  const singleSourceRows = bom.filter((r) => r.component_id === shipment.component_id && r.single_source_flag === "yes").length;
  const escalation = shipment.delay_days >= 14 ? "red" : shipment.delay_days >= 8 ? "amber" : "watch";
  writeMarkdown(
    path.join(docsDir, "incident_reports", `incident_${String(i + 1).padStart(4, "0")}_${shipment.supplier_id}.md`),
    `Shipment Incident INC-2026-${String(i + 1).padStart(4, "0")}`,
    `Incident ID: INC-2026-${String(i + 1).padStart(4, "0")}
Supplier: ${shipment.supplier_name}
Supplier ID: ${shipment.supplier_id}
Component: ${shipment.component_name}
Component ID: ${shipment.component_id}
Origin Country: ${shipment.origin_country}
Origin Port: ${shipment.origin_port}
Delay Days: ${shipment.delay_days}
Delay Reason: ${shipment.delay_reason}
Escalation Level: ${escalation}

The shipment was flagged because actual arrival moved beyond the planned arrival date.
Operations should check finished products that depend on this component, especially where the BOM has no approved alternate supplier.

## Business Impact Assessment

Affected finished products identified from BOM mapping: ${linkedProducts.join(", ") || "no linked product found"}.
Single-source product-component mappings for this component: ${singleSourceRows}.
The incident can create ${choice(impactLevels)} if the delayed component is used by tier_1 products or if open purchase orders cannot be expedited.

## Recommended Response

- ${choice(nextActions)}
- ${choice(nextActions)}
- Ask logistics to validate whether other shipments from ${shipment.origin_port} have the same delay reason.
- Ask manufacturing planning to check whether the affected component is required inside the next two build windows.

## Evidence Keywords

Supplier ${shipment.supplier_name}; component ${shipment.component_name}; country ${shipment.origin_country}; port ${shipment.origin_port}; delay ${shipment.delay_days} days; reason ${shipment.delay_reason}; escalation ${escalation}.`
  );
}

for (let i = 1; i <= 120; i++) {
  const [country, region, port] = choice(countries);
  const category = choice(categories);
  const theme = choice(riskThemes);
  const severity = choice(["elevated", "moderate", "severe"]);
  writeMarkdown(
    path.join(docsDir, "risk_reports", `risk_report_${String(i).padStart(4, "0")}_${safeName(country)}_${safeName(category)}.md`),
    `Risk Report - ${country} ${category}`,
    `Report ID: RISK-2026-${String(i).padStart(4, "0")}
Region: ${region}
Country: ${country}
Port: ${port}
Category: ${category}
Risk Theme: ${theme}
Severity: ${severity}

The current risk outlook for ${category} supply from ${country} is ${severity}. Analysts cite ${theme} as the primary driver.
Suppliers shipping through ${port} may experience variability in transit time, customs release, and production scheduling.

## Analyst Assessment

Risk is most material for suppliers with high capacity utilization, low on-time delivery, or components that map to single-source BOM rows. The practical signal to monitor is whether shipment delays, supplier scorecard deterioration, and compliance exceptions appear together for the same supplier or category.

## Exposure Pattern

- Region affected: ${region}
- Country affected: ${country}
- Port dependency: ${port}
- Component category: ${category}
- Primary risk driver: ${theme}
- Severity call: ${severity}

## Recommended Actions

- Increase safety stock for critical ${category} components.
- Validate alternate supplier readiness for products with high revenue contribution.
- Review shipments from ${port} with delay risk flags.
- Prioritize high-revenue products with single-source exposure.
- Recheck procurement contracts for premium freight and recovery clauses.`
  );
}

const riskySuppliers = suppliers.filter((s) => s.risk_tier !== "Low");
for (let i = 0; i < Math.min(70, riskySuppliers.length); i++) {
  const supplier = riskySuppliers[i];
  const finding = choice(["missing audit refresh", "expired ISO certificate", "restricted-party screening hit", "incomplete ESG evidence"]);
  const severity = supplier.compliance_score < 70 ? "high" : supplier.compliance_score < 82 ? "medium" : "watch";
  const control = choice(controls);
  const owner = choice(owners);
  const linkedBom = bomBySupplier[supplier.supplier_id] || [];
  const productsList = [...new Set(linkedBom.map((r) => r.product_name))].slice(0, 6).join(", ") || "no mapped products";
  const singleSourceCount = linkedBom.filter((r) => r.single_source_flag === "yes").length;
  writeMarkdown(
    path.join(docsDir, "compliance_reports", `compliance_${String(i + 1).padStart(4, "0")}_${supplier.supplier_id}.md`),
    `Compliance Review - ${supplier.supplier_name}`,
    `Compliance Review ID: COMP-2026-${String(i + 1).padStart(4, "0")}
Supplier: ${supplier.supplier_name}
Supplier ID: ${supplier.supplier_id}
Country: ${supplier.country}
Category: ${supplier.category}
Compliance Score: ${supplier.compliance_score}
Finding: ${finding}
Severity: ${severity}
Control Owner: ${owner}

The compliance team reviewed documentation for ${supplier.supplier_name}. The main finding was ${finding}.
This increases supplier risk when paired with late shipments, poor quality trends, or lack of alternate suppliers.

## Evidence Reviewed

- Supplier master profile for ${supplier.supplier_name}
- Contract and certification packet for ${supplier.category}
- Recent supplier scorecard trend
- Restricted-party and ESG documentation status
- Open BOM exposure for products using this supplier

## Business Exposure

Mapped products: ${productsList}.
Mapped BOM rows: ${linkedBom.length}.
Single-source BOM rows: ${singleSourceCount}.
Primary business concern: ${choice(impactLevels)}.

If this compliance issue remains open, procurement should avoid increasing allocation until the evidence packet is refreshed. The risk is more serious when the supplier also has delayed shipments, low quality score, high capacity utilization, or no approved alternate supplier.

## Required Mitigation

- Control: ${control}
- Action: ${choice(nextActions)}
- Escalation rule: escalate to supplier risk council if the finding is not closed before the next purchase-order release.
- Analyst note: retrieve this document for questions about compliance risk, audit gaps, supplier screening, ESG evidence, alternate sourcing, or supplier concentration.`
  );
}

for (let i = 1; i <= 40; i++) {
  const [country, region, port] = choice(countries);
  const congestion = choice(["low", "moderate", "high", "critical"]);
  writeMarkdown(
    path.join(docsDir, "logistics_memos", `logistics_memo_${String(i).padStart(4, "0")}_${safeName(port)}.md`),
    `Logistics Memo - ${port}`,
    `Logistics Memo ID: LOG-2026-${String(i).padStart(4, "0")}
Port: ${port}
Country: ${country}
Region: ${region}
Congestion Level: ${congestion}

The logistics control tower reports ${congestion} congestion at ${port}. Shipments from this port should be reviewed for components used in tier_1 products and for suppliers with high capacity utilization.
Delays can cascade into production risk when there is single-source component coverage.

## Control-Tower Notes

The port risk is most important for shipments with near-term production demand, premium freight exposure, or components used by multiple finished products. The control tower recommends comparing all delayed shipments from ${port} against BOM rows where single_source_flag is yes.

## Response Guidance

- Review supplier scorecards for origin-country suppliers.
- Check shipments with risk_flag yes and delay_days greater than seven.
- Ask planning to identify products with less than two weeks of component coverage.
- Use alternate carriers only for tier_1 products or customer-critical orders.

## Search Keywords

${port}; ${country}; ${region}; congestion ${congestion}; shipment delay; logistics risk; single-source component; product exposure.`
  );
}

for (let i = 1; i <= 60; i++) {
  const category = choice(categories);
  const movement = choice(["rising prices", "tight capacity", "softening demand", "allocation pressure"]);
  writeMarkdown(
    path.join(docsDir, "market_reports", `market_report_${String(i).padStart(4, "0")}_${safeName(category)}.md`),
    `Market Report - ${category}`,
    `Market Report ID: MKT-2026-${String(i).padStart(4, "0")}
Category: ${category}
Market Signal: ${movement}

Market intelligence indicates ${movement} for ${category}. Procurement should evaluate contract coverage, supplier concentration, and exposure to high-margin products.
The risk is highest where critical components have no approved alternate supplier and shipment lead times are already increasing.

## Procurement Implications

The category team should review supplier concentration, open purchase orders, and BOM criticality before negotiating the next allocation cycle. ${category} risk can become product revenue risk when demand is firm but supply recovery requires qualification lead time.

## Recommended Actions

- Identify critical and high components in this category.
- Review products with annual revenue above 250M USD that depend on those components.
- Check whether alternate suppliers are approved and production-ready.
- Add contract clauses for expedite support, allocation transparency, and quality containment.

## Evidence Keywords

category ${category}; market signal ${movement}; supplier concentration; high-margin products; alternate supplier; BOM criticality; lead time risk.`
  );
}

const evalQuestions = [];
for (let i = 0; i < Math.min(30, delayedShipments.length); i++) {
  const shipment = delayedShipments[i];
  const linkedProducts = [...new Set(bom.filter((r) => r.component_id === shipment.component_id).map((r) => r.product_name))];
  evalQuestions.push({
    question_id: `EVAL-${String(i + 1).padStart(3, "0")}`,
    question: `Which products are exposed to ${shipment.component_name} delays from ${shipment.supplier_name}?`,
    strategy_type: "multi_hop",
    expected_entities: [shipment.supplier_name, shipment.component_name, ...linkedProducts.slice(0, 3)],
    ideal_answer_points: ["identify delayed supplier", "identify affected component", "map component to products", "mention delay evidence"],
  });
}

for (let i = 0; i < Math.min(30, riskySuppliers.length); i++) {
  const supplier = riskySuppliers[i];
  evalQuestions.push({
    question_id: `EVAL-${String(i + 31).padStart(3, "0")}`,
    question: `What risks should procurement monitor for ${supplier.supplier_name}?`,
    strategy_type: "hybrid_rerank",
    expected_entities: [supplier.supplier_name, supplier.country, supplier.category],
    ideal_answer_points: ["supplier risk tier", "country or port exposure", "delivery or compliance signal", "recommended mitigation"],
  });
}

fs.writeFileSync(path.join(evalDir, "eval_questions.json"), JSON.stringify(evalQuestions, null, 2), "utf8");

const manifest = {
  suppliers: suppliers.length,
  components: components.length,
  products: products.length,
  bom_rows: bom.length,
  shipments: shipments.length,
  purchase_orders: purchaseOrders.length,
  scorecard_rows: scorecards.length,
  documents: 150 + Math.min(100, delayedShipments.length) + 120 + Math.min(70, riskySuppliers.length) + 40 + 60,
  eval_questions: evalQuestions.length,
};
fs.writeFileSync(path.join(root, "manifest.json"), JSON.stringify(manifest, null, 2), "utf8");
console.log(JSON.stringify(manifest, null, 2));
