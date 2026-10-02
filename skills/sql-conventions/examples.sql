WITH orders_q1 AS (
    SELECT order_id, region, amount
    FROM sales.orders
    WHERE order_date >= DATE '2026-01-01'
      AND order_date < DATE '2026-04-01'
),
revenue_by_region AS (
    SELECT region, SUM(amount) AS revenue
    FROM orders_q1
    GROUP BY region
)
SELECT region, revenue
FROM revenue_by_region
ORDER BY revenue DESC
-- source: sql-conventions
