-- Total Revenue

SELECT
SUM(total_amount) AS total_revenue
FROM orders;



-- Total Orders

SELECT
COUNT(order_id) AS total_orders
FROM orders;



-- Average Order Value

SELECT
ROUND(
AVG(total_amount),
2
) AS average_order_value
FROM orders;



-- Top 10 Products by Revenue

SELECT
p.title,
ROUND(
SUM(oi.total_price),
2
) AS revenue

FROM order_items oi

JOIN products p
ON oi.product_id=p.product_id

GROUP BY p.title

ORDER BY revenue DESC

LIMIT 10;



-- Revenue by State

SELECT
c.state,

ROUND(
SUM(o.total_amount),
2
) AS revenue

FROM customers c

JOIN orders o
ON c.customer_id=o.customer_id

GROUP BY c.state

ORDER BY revenue DESC;



-- Daily Sales Trend

SELECT
order_date,

ROUND(
SUM(total_amount),
2
) AS daily_sales

FROM orders

GROUP BY order_date

ORDER BY order_date;
