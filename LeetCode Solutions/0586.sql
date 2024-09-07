WITH OrderCounts AS (
    SELECT customer_number, COUNT(*) AS order_count
    FROM Orders
    GROUP BY customer_number
),
MaxOrderCount AS (
    SELECT MAX(order_count) AS max_count
    FROM OrderCounts
)
SELECT customer_number
FROM OrderCounts
WHERE order_count = (SELECT max_count FROM MaxOrderCount);
