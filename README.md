# Superstore Sales Analysis

An end-to-end data analysis project on retail sales data, using **Python**, **MySQL**, **Excel**, and **Power BI**.

![Dashboard](powerbi/dashboard.png)

## Project Overview

The goal of this project is to analyze four years of retail sales (2015–2018) and answer practical business questions: which regions perform best, which products sell most, how sales change across the year, and whether faster shipping really delivers faster.

## Dataset

- **Source:** [Superstore Sales Dataset on Kaggle](https://www.kaggle.com/) *(add the exact link to the dataset page you downloaded)*
- **Size:** 9,800 orders, 18 original columns
- **Period:** 3 Jan 2015 – 30 Dec 2018
- **Scope:** United States, 4 regions, 3 product categories, 17 sub-categories, 793 customers

## Tools Used

| Tool | Purpose |
|---|---|
| Python (pandas, SQLAlchemy) | Data exploration, cleaning, and loading into MySQL |
| MySQL | Analytical queries to answer business questions |
| Excel | Pivot tables and charts for a business-friendly report |
| Power BI | Interactive dashboard |

## Project Structure

```
superstore-sales-analysis/
├── data/          # Cleaned dataset (CSV)
├── python/        # Cleaning and MySQL loading script
├── sql/           # Analysis queries with commented insights
├── excel/         # Pivot tables and charts workbook
├── powerbi/       # Dashboard file and screenshot
└── README.md
```

## Workflow

### 1. Exploration and Cleaning (Python)
- Inspected structure, data types, and missing values
- **Postal Code** had 11 missing values, all from Burlington, Vermont. Since three different US cities share the name "Burlington", filling the value from another row would have been wrong. The column is not used in the analysis, so the values were left empty on purpose
- Converted `Order Date` and `Ship Date` to real dates. The format was day/month/year, confirmed by values such as `15/04/2018`
- Created a new column, **Shipping Duration** (days between order and shipping), and validated it (min = 0, max = 7 days)
- Detected **1,145 outliers** in `Sales` using the IQR method (upper bound ≈ 500.64). They were kept: most are Furniture and Technology items, which are naturally higher priced, so they are real sales and not errors

### 2. Analysis (MySQL)
Five queries answer the main business questions. See [`sql/superstore_analysis.sql`](sql/superstore_analysis.sql).

### 3. Reporting (Excel)
Three pivot tables (region, sub-category, monthly trend) with a chart. All figures were cross-checked against the SQL results, and they match.

### 4. Dashboard (Power BI)
An interactive dashboard with KPI cards, region, category, monthly trend, and top sub-category charts, plus slicers for Category, Region, Segment, and Ship Mode.

## Key Findings

- **Total sales:** about $2.26M across 9,800 orders, with an average order value of about $230.77
- **West** is the strongest region (about $710K), while **South** is the weakest (about $389K), a gap of roughly 83%
- **Binders** (1,492 orders) and **Paper** (1,338) are the most frequently ordered sub-categories. Order volume and revenue are different questions, so cheap items can lead the first without leading the second
- **Strong seasonality:** sales peak in November and December and dip in January and February, every year
- **Year-over-year growth:** 2018 was the strongest year (about $722K) versus about $480K in 2015, with the best single month in November 2018 (about $118K)
- **Shipping delivers on its promise:** Same Day (~0.04 days), First Class (~2.2), Second Class (~3.2), Standard Class (~5.0)
- The top customer, Sean Miller (about $25K), is driven mostly by one $22.6K order for a Cisco TelePresence system, so a "top customer" ranking can be skewed by a single large purchase

## How to Run

1. Clone the repository
2. Install dependencies: `pip install pandas sqlalchemy mysql-connector-python python-dotenv`
3. Create a `.env` file in the project root:
   ```
   DB_HOST=localhost
   DB_USER=your_user
   DB_PASSWORD=your_password
   ```
4. Run `python/import_superstore.py` to load the data into MySQL
5. Run the queries in `sql/superstore_analysis.sql`

## Author

**Youssef Moamen**
[LinkedIn](www.linkedin.com/in/youssef-moamen-900b0343a) · [GitHub](https://github.com/youssefmoamen-data-analytics)
