-- ============================================================
-- Superstore Sales Analysis
-- Database: superstore_db | Table: sales
-- ============================================================


-- ============================================================
-- 1. Total Sales by Region
-- Business question: Which region generates the most revenue?
-- ============================================================

SELECT Region, SUM(Sales) AS Total_Sales
FROM superstore_db.sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Insight: West is the strongest region (~710K), South is the
-- weakest (~389K) — a ~83% gap worth investigating further.


-- ============================================================
-- 2. Most Ordered Sub-Categories
-- Business question: Which products are ordered most often?
-- (Order count, not revenue — a cheap item can still top this list)
-- ============================================================

SELECT `Sub-Category`, COUNT(*) AS Order_Count
FROM superstore_db.sales
GROUP BY `Sub-Category`
ORDER BY Order_Count DESC;

-- Insight: Binders (1492 orders) and Paper (1338) lead by volume,
-- but that doesn't mean they lead by revenue — volume vs. value
-- are two different questions.


-- ============================================================
-- 3. Top 10 Customers by Total Sales
-- Business question: Who are our highest-value customers?
-- ============================================================

SELECT `Customer Name`, SUM(Sales) AS Total_Sales
FROM superstore_db.sales
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;

-- Insight: Sean Miller tops the list (~25K), largely driven by a
-- single high-value order (a Cisco TelePresence system, ~22.6K).
-- A single large order can skew a "top customer" ranking —
-- worth checking purchase frequency too, not just total value.


-- ============================================================
-- 4. Average Shipping Duration by Ship Mode
-- Business question: Does paying for faster shipping actually
-- get the order there faster?
-- ============================================================

SELECT `Ship Mode`, AVG(`Shipping Duration`) AS Avg_Shipping_Duration
FROM superstore_db.sales
GROUP BY `Ship Mode`;

-- Insight: Same Day (~0.04 days) < First Class (~2.18) <
-- Second Class (~3.25) < Standard Class (~5.01).
-- The ranking matches expectations — premium shipping delivers
-- real value, not just a marketing label.


-- ============================================================
-- 5. Monthly Sales Trend by Year
-- Business question: Is there a seasonal pattern, and is the
-- business growing year over year?
-- ============================================================

SELECT YEAR(`Order Date`) AS Order_Year,
       MONTH(`Order Date`) AS Order_Month,
       SUM(Sales) AS Total_Sales
FROM superstore_db.sales
GROUP BY YEAR(`Order Date`), MONTH(`Order Date`)
ORDER BY Order_Year, Order_Month;

-- Insight: Clear seasonality every year — sales peak in
-- November/December (holiday season) and dip in Jan/Feb.
-- 2018 shows the strongest November (~118K), suggesting
-- year-over-year growth on top of the seasonal pattern.


-- ============================================================
-- Sanity Check: Data Date Range
-- Confirms the full time span this analysis covers
-- ============================================================

SELECT MIN(`Order Date`) AS Earliest_Date, MAX(`Order Date`) AS Latest_Date
FROM superstore_db.sales;

-- Result: 2015-01-03 to 2018-12-30 (4 full years of data)