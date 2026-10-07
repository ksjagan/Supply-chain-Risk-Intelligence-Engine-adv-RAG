# Supply Chain Risk Intelligence Engine

An enterprise-style retrieval and reasoning project for answering complex supply chain risk questions across structured tables and unstructured business documents.

## Real Problem

Supply chain teams need to answer questions that require connecting supplier profiles, shipment delays, incident reports, product BOMs, compliance findings, and regional risk memos. Normal keyword search and simple vector search miss the relationships between suppliers, components, products, and operational risks.

This project builds a higher-accuracy retrieval engine using hybrid search, reranking, query rewriting, multi-query retrieval, and multi-hop reasoning.

## Build Data

```bash
python data/generate_data.py
```

Or, if you prefer module execution:

```bash
python -m data.generate_data
```

This creates `data/company_data` with synthetic but realistic enterprise data:

- 150 suppliers
- 400 components
- 80 products
- 500+ BOM rows
- 1,500 purchase orders
- 2,500 shipments
- 1,200 supplier scorecards
- 500+ markdown documents
- 60 evaluation questions

## Run API

```bash
uvicorn app.main:app --reload
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## Run Streamlit UI

```bash
streamlit run streamlit_app.py
```

The Streamlit app is the only user interface. It includes:

- Chat interface
- Retrieval strategy selector
- Risk score panel
- Query rewrite and multi-hop trace
- Retrieved evidence expanders

Open:

```text
http://localhost:8501
```

## Notebook

Open:

```text
notebooks/supply_chain_risk_retrieval_engine.ipynb
```

The notebook is a standalone backend demo. It contains the full pipeline code inline so you can explain every step without jumping into the `app/` folder.

## Demo Questions

- Which products are most exposed to delayed semiconductor shipments from Malaysia?
- Which suppliers create single-source risk for high-revenue products?
- What components are affected by Vietnam port congestion?
- Which suppliers have both poor delivery performance and compliance risk?
- What are the biggest supply chain risks for the Orion product line?
