WITH Revenue AS (
    SELECT
        p.product_id,
        SUM(u.units * p.price) AS total_revenue,
        SUM(u.units) AS total_units
    FROM Prices p
    LEFT JOIN UnitsSold u
        ON p.product_id = u.product_id
        AND u.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY p.product_id
),
AveragePrice AS (
    SELECT
        r.product_id,
        COALESCE(total_revenue / NULLIF(total_units, 0), 0) AS average_price
    FROM Revenue r
)
SELECT
    product_id,
    ROUND(average_price, 2) AS average_price
FROM AveragePrice
