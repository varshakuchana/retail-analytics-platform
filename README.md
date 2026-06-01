# Retail Analytics Platform

## Overview

Retail Analytics Platform is an end-to-end data analytics project that simulates a retail business intelligence workflow. The project collects product data from a public API, generates realistic customer and transaction data, stores data in PostgreSQL, performs SQL based analysis, and visualizes business insights using Tableau.

The dashboard helps analyze sales performance, product demand, regional revenue, and customer segment behavior.

## Live Dashboard

https://public.tableau.com/app/profile/varsha.kuchana/viz/RetailAnalyticsPlatform/RetailAnalyticsPlatform

## Dashboard Preview

![Dashboard](./screenshots/Retail%20Analytics.png)

![Dashboard Filters](./screenshots/Retail%20Analytics%202.png)

## Tech Stack

- Python
- Pandas
- Requests
- PostgreSQL
- SQLAlchemy
- SQL
- Tableau Public

## Project Workflow

DummyJSON API
        ↓
Python ETL Scripts
        ↓
PostgreSQL Database
        ↓
SQL Analysis
        ↓
Dashboard Dataset
        ↓
Tableau Dashboard

## Key Features

- Retrieved product data from the DummyJSON public API
- Generated realistic customer, order, and order item data using Python
- Designed PostgreSQL tables for products, customers, orders, and order items
- Loaded data into PostgreSQL using Python and SQLAlchemy
- Wrote SQL queries for revenue, orders, average value, top products, and state wise sales
- Exported dashboard-ready data for Tableau
- Built an interactive Tableau dashboard with filters and KPI cards

## Dashboard Metrics

- Total Revenue
- Total Quantity Sold
- Average Order Value
- Total Orders
- Sales Trend
- Revenue by State
- Top Products by Revenue
- Top Products by Quantity
- Customer Segment Distribution

## Key Insights

- Revenue and quantity metrics provide different views of product performance.
- High revenue products are not always the highest selling products by quantity.
- Regional revenue analysis helps identify stronger performing states.
- Customer segment analysis helps compare revenue contribution from New, Returning, and VIP customers.

## Future Improvements

- Add live database connection to Tableau
- Automate data refresh
- Add profit margin analysis
- Add forecasting for future sales trends
- Deploy a web version using Streamlit or Power BI Service
