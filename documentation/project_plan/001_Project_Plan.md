# Retail Intelligence Platform

# 001 Project Plan

**Version:** 2.0  
**Project:** Retail Intelligence Platform  
**Prepared By:** Divya Kumar  
**Status:** Completed – Version 1 Final Delivery

---

# 1. Document Purpose

This Project Plan defines the business context, analytical scope, execution roadmap, deliverables, and final delivery structure of the **Retail Intelligence Platform**.

The document serves as the master planning and governance artifact for the project and is intended to:

- define the business problem and analytical objectives
- document the scope of the project
- summarize the implementation roadmap and sprint execution
- list final deliverables produced across notebooks, reports, and dashboards
- provide a clear reference for portfolio review, interviews, and future project extension

This document should be read together with:

- **002_Data_Dictionary.md** – enterprise data model, table definitions, keys, and business rules
- **README.md** – repository setup, project overview, and usage instructions

---

# 2. Executive Summary

The **Retail Intelligence Platform** is an end-to-end e-commerce analytics project built using the **Olist Brazilian E-Commerce dataset**. The objective of the project is to transform raw marketplace transaction data into a structured business intelligence solution that supports analysis across customers, orders, products, payments, sellers, reviews, retention, and market basket behavior.

The project combines:

- **Python-based data preparation and analytics**
- **report-ready CSV generation**
- **customer segmentation and retention analysis**
- **seller and marketplace analytics**
- **market basket / association rule analysis**
- **Streamlit-based multi-page analytics application**
- **project documentation and governance artifacts**

The final outcome is a portfolio-ready analytics platform that demonstrates the ability to move from raw relational data to reusable business reporting assets and interactive dashboards.

---

# 3. Business Problem Statement

E-commerce marketplaces generate large volumes of data across multiple business functions such as orders, payments, products, logistics, customer reviews, and seller operations. However, raw data in isolated tables does not directly support decision-making.

Business stakeholders require an integrated analytical view to answer questions such as:

- How many customers are active, repeat, and high value?
- Which customer segments contribute the most revenue?
- What does repeat purchase behavior look like?
- Which sellers generate the highest revenue and order volume?
- Which product categories dominate sales and transaction baskets?
- Which products or categories are frequently purchased together?
- How do reviews and seller performance reflect marketplace quality?

The Retail Intelligence Platform was built to solve this by creating a structured analytics layer on top of the raw Olist dataset.

---

# 4. Project Objectives

The project was designed with the following objectives:

## 4.1 Primary Objectives

1. Build a reusable analytics project on top of a real-world e-commerce dataset.
2. Create a clean, documented data foundation for business reporting.
3. Generate business-ready outputs for customer, seller, and basket analysis.
4. Build a Streamlit dashboard application to surface insights interactively.
5. Demonstrate end-to-end analytics capability across data understanding, transformation, KPI generation, and dashboarding.

## 4.2 Analytical Objectives

The platform should support analysis of:

- customer behavior and segmentation
- repeat purchase and retention behavior
- seller / marketplace performance
- product category performance
- payment behavior
- customer reviews and satisfaction
- basket-level product association opportunities

---

# 5. Dataset and Analytical Context

The project uses the **Olist Brazilian E-Commerce Public Dataset**, which contains marketplace transaction data from Brazil across approximately 2016–2018.

The dataset includes multiple relational tables covering:

- customers
- orders
- order items
- payments
- reviews
- products
- sellers
- geolocation
- category translation

These tables were used to build a business-oriented analytics model for reporting and dashboard consumption.

Detailed table definitions, keys, relationships, and business rules are documented in **002_Data_Dictionary.md**.

---

# 6. Scope of the Project

# 6.1 In Scope

The following capabilities are included in Version 1 of the Retail Intelligence Platform:

## Data Understanding and Preparation
- profiling and understanding of core Olist datasets
- identification of keys, joins, and business grain
- data cleaning and standardization for analytics use
- translation / harmonization of product categories where needed

## Python Analytics
- customer-level aggregation and behavioral analysis
- repeat purchase analysis
- cohort-style retention summary generation
- RFM-style customer segmentation outputs
- seller performance analytics
- seller review summary analytics
- seller category summary analytics
- market basket / association rule analysis
- top category basket presence analysis
- basket diagnostics summaries

## Reporting Outputs
Creation of report-ready CSV outputs for use in Streamlit and downstream reporting.

## Dashboarding / Application Layer
Development of a multi-page **Streamlit analytics application** with dedicated pages for:
- Home
- Executive Dashboard
- Customer Segmentation
- Cohort Retention Analysis
- Market Basket Analysis
- Seller / Marketplace Analytics

## Documentation
Creation of:
- Project Plan
- Data Dictionary
- README
- project structure and execution notes

---

# 6.2 Out of Scope

The following items are outside the scope of Version 1:

- production-grade data pipelines / orchestration
- cloud deployment and infrastructure automation
- live database hosting / enterprise data warehouse deployment
- authentication / role-based access control
- real-time data ingestion
- advanced machine learning recommendation engines
- full-stack custom web application development beyond Streamlit analytics delivery
- enterprise MLOps / CI-CD pipelines
- forecasting productionization beyond exploratory project scope

---

# 7. Key Business Questions Addressed

The project was designed to answer business questions across several domains.

## 7.1 Customer and Retention
- How many unique customers does the business have?
- How many customers are repeat customers?
- What is the repeat purchase rate?
- What is the average customer spend?
- Which customer segments contribute the highest monetary value?
- What does customer frequency and recency behavior look like?

## 7.2 Seller / Marketplace
- Which sellers generate the highest revenue?
- Which sellers fulfill the highest number of orders?
- What is the average review quality across sellers?
- Which product categories contribute the most seller revenue?
- Is marketplace performance concentrated among a small number of sellers?

## 7.3 Basket and Product Affinity
- Which product categories appear most frequently in transaction baskets?
- What is the basket size distribution?
- Which product or category combinations are associated with one another?
- What bundling or cross-sell opportunities are suggested by lift and confidence metrics?

## 7.4 Executive Monitoring
- What is the overall customer and repeat-customer profile of the business?
- Which segments contribute the most value?
- Which report assets are currently available in the analytics layer?

---

# 8. Project Deliverables

The final Version 1 project includes the following deliverables.

# 8.1 Documentation Deliverables
- `001_Project_Plan.md`
- `002_Data_Dictionary.md`
- `README.md`

# 8.2 Analytics / Notebook Deliverables
Python notebooks and/or notebook sections that produce:
- customer segmentation outputs
- repeat purchase summaries
- cohort business summaries
- market basket outputs
- seller performance summaries
- seller review summaries
- seller category summaries

# 8.3 Report Output Deliverables
Report-ready CSV files generated for dashboard consumption, including project outputs such as:

- `rfm_customer_segments.csv`
- `repeat_purchase_summary.csv`
- `cohort_business_summary.csv`
- `association_rules.csv`
- `basket_summary.csv`
- `top_categories_by_order_presence.csv`
- `seller_performance_summary.csv`
- `seller_review_summary.csv`
- `seller_category_summary.csv`

## Note
The exact contents of the `reports/` folder depend on the final export blocks used in the project, but the above files represent the intended analytics output layer for the Streamlit application.

# 8.4 Streamlit Application Deliverables
The project includes a multi-page Streamlit application under the `app/` directory with pages for:

- Home
- Executive Dashboard
- Customer Segmentation
- Cohort Retention Analysis
- Market Basket Analysis
- Seller / Marketplace Analytics

---

# 9. Final Repository / Solution Architecture

At a high level, the Retail Intelligence Platform follows the architecture below.

## 9.1 Raw Data Layer
Raw Olist CSV datasets stored in the project data layer.

## 9.2 Analytics / Transformation Layer
Python notebooks and scripts used to:
- clean data
- join datasets
- compute KPIs
- generate customer / seller / basket summaries
- export report-ready CSV outputs

## 9.3 Reporting Layer
Generated CSV outputs stored in the reports directory and consumed by the dashboard application.

## 9.4 Presentation Layer
A Streamlit multi-page application that reads the generated CSV outputs and presents business insights visually.

---

# 10. Project Execution Approach

The project was executed in phased form, moving from planning and data understanding into analytics development and dashboard delivery.

## Phase 1 – Project Planning and Repository Setup
- define project scope
- establish folder structure
- create planning documentation
- identify core business questions

## Phase 2 – Data Understanding and Data Dictionary
- review source datasets
- understand table grain, keys, and relationships
- document data structure in the Enterprise Data Dictionary

## Phase 3 – Data Cleaning and Analytical Preparation
- create clean analysis-ready tables / joins
- standardize column usage and business definitions
- prepare intermediate logic for customer, seller, and basket analysis

## Phase 4 – Customer Analytics and Retention Layer
- repeat purchase summary
- cohort-style customer summary
- RFM segmentation outputs

## Phase 5 – Market Basket and Affinity Analytics
- build basket matrix / category basket logic
- generate association rules
- export basket diagnostics and top category presence summaries

## Phase 6 – Seller / Marketplace Analytics
- seller revenue and order analysis
- seller review summary
- seller category contribution analysis

## Phase 7 – Streamlit Dashboard Development
- build multi-page application
- connect dashboard pages to report CSVs
- create KPI cards, charts, and summary tables
- add business interpretation notes

## Phase 8 – Documentation and Finalization
- finalize README
- finalize Project Plan
- finalize Data Dictionary
- validate repo structure and dashboard readiness

---

# 11. Sprint Summary

The project evolved over multiple implementation sprints. The final summary of the major workstreams is shown below.

| Sprint / Workstream | Description | Final Status |
| --- | --- | --- |
| Sprint 1 | Project setup, scope definition, folder structure | Completed |
| Sprint 2 | Data understanding and table documentation | Completed |
| Sprint 3 | Data cleaning and analytical preparation | Completed |
| Sprint 4 | Customer and repeat purchase analytics | Completed |
| Sprint 5 | Cohort and RFM outputs | Completed |
| Sprint 6 | Market basket analytics and association rules | Completed |
| Sprint 7 | Seller / marketplace analytics | Completed |
| Sprint 8 | Streamlit application build and page integration | Completed |
| Sprint 9 | README, documentation, and repo finalization | Completed |

---

# 12. Final Modules Delivered

The following Streamlit modules were delivered in Version 1.

## 12.1 Home
Landing page for the Retail Intelligence Platform with navigation and project overview.

## 12.2 Executive Dashboard
High-level business summary page focused on:
- total customers
- repeat customers
- repeat rate
- average customer spend
- segment distribution
- segment revenue contribution
- data asset readiness

## 12.3 Customer Segmentation
Customer analytics page focused on:
- RFM customer segments
- segment distribution
- revenue by segment
- repeat purchase summary
- RFM sample records

## 12.4 Cohort Retention Analysis
Retention-focused page summarizing:
- repeat customers
- average orders per customer
- average customer spend
- cohort business summary
- repeat purchase distribution

## 12.5 Market Basket Analysis
Basket analytics page focused on:
- association rules
- average lift / confidence
- top categories by order presence
- basket summary outputs
- bundling and cross-sell interpretation

## 12.6 Seller / Marketplace Analytics
Seller-focused page summarizing:
- total sellers
- top seller revenue
- average seller orders
- seller review quality
- seller performance table
- seller review summary
- seller category revenue analysis

---

# 13. Tools and Technology Stack

The project uses the following technologies.

## Programming and Analytics
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- SciPy
- statsmodels
- mlxtend

## Notebook / Development Environment
- Jupyter Notebook
- ipykernel

## File / Excel Support
- openpyxl
- xlsxwriter

## Dashboarding
- Streamlit
- Plotly Express

## Documentation
- Markdown
- GitHub repository documentation

---

# 14. Folder-Level Project Components

The project repository is organized around the following logical components.

## `app/`
Contains the Streamlit application, including the main launcher and page modules.

## `reports/`
Contains report-ready CSV outputs generated by the analytics notebooks and consumed by the Streamlit pages.

## `notebooks/`
Contains notebook-based analytics work for data understanding, transformations, customer analytics, seller analytics, and basket analysis.

## `src/`
Contains shared helper logic such as constants, KPI helpers, and common utility functions used by the Streamlit app.

## `project_plan/`
Contains project-level documentation including:
- Project Plan
- Data Dictionary

---

# 15. Risks Encountered During Project Execution

The following implementation risks and challenges were encountered during development.

## 15.1 Export Synchronization Risk
Some Streamlit pages depended on report CSVs that were not initially exported or were exported under inconsistent names. This required alignment between notebook outputs and dashboard expectations.

## 15.2 Column Naming Inconsistency
Different notebook outputs occasionally used slightly different column names for the same concept, requiring standardization logic inside the dashboard pages.

## 15.3 Path and File Management Issues
Several export blocks required adjustment to ensure files were saved to the correct output directory and consumed consistently by the Streamlit app.

## 15.4 Page / App Integration Issues
Some Streamlit pages initially broke due to missing imports, mismatched file names, or syntax errors that had to be resolved during final integration.

## 15.5 Scope Expansion During Delivery
The project expanded beyond simple sales reporting into seller analytics, customer segmentation, retention summaries, and basket analysis. This improved project value but increased coordination across notebooks, exports, and pages.

---

# 16. Success Criteria

The project is considered successful for Version 1 if the following conditions are met:

1. Core Olist datasets are documented and understood.
2. Report-ready analytical outputs are generated for the major business modules.
3. The Streamlit application loads the required report files without structural errors.
4. Customer segmentation, retention, seller, and basket analytics are available in the app.
5. Documentation exists for both project planning and enterprise data structure.
6. The repository is strong enough to be presented as a portfolio project and discussed in interviews.

---

# 17. Final Project Status

**Project Status:** Completed – Version 1 Final Delivery

Version 1 of the Retail Intelligence Platform has been completed as a portfolio-grade analytics project. The project includes:

- a documented data model
- Python-based analytical outputs
- report CSV generation
- a multi-page Streamlit analytics application
- project documentation for planning and data governance

The platform is now suitable for:

- GitHub portfolio presentation
- resume project showcase
- interview discussion around end-to-end analytics delivery
- future enhancement into Version 2 features

---

# 18. Future Enhancements

Potential future enhancements include:

- state-wise and city-wise sales dashboards
- payment analytics page
- delivery / logistics performance dashboard
- review sentiment analysis
- advanced cohort heatmaps
- product-level recommendation modeling
- sales forecasting module integration into Streamlit
- SQL layer formalization for reproducible analytical marts
- deployment of the Streamlit app to a hosted environment

---

# 19. Relationship to the Data Dictionary

This Project Plan defines the **business scope, execution roadmap, and final deliverables** of the Retail Intelligence Platform.

The companion document **`002_Data_Dictionary.md`** defines the **data model, table structures, relationships, keys, business rules, and data quality expectations** that support the project’s analytical outputs.

Together, the two documents form the core governance and documentation layer of the project.

---

# 20. Final Conclusion

The Retail Intelligence Platform demonstrates an end-to-end analytics workflow built on a multi-table e-commerce dataset. The project moves from raw source data to documented analytical assets, reusable reporting outputs, and a dashboard application designed for business insight consumption.

The project showcases capabilities across:

- business problem framing
- data understanding
- data documentation
- analytical transformation
- KPI design
- customer and seller analytics
- market basket analysis
- dashboard development
- project documentation and final delivery

This concludes **Version 1** of the Retail Intelligence Platform project.

---

**End of 001 Project Plan**