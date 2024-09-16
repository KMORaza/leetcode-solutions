WITH LatestPrices AS (
    SELECT
        product_id,
        MAX(change_date) AS latest_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
),
ProductPrices AS (
    SELECT
        p.product_id,
        p.new_price
    FROM Products p
    JOIN LatestPrices lp
    ON p.product_id = lp.product_id
    AND p.change_date = lp.latest_date
)
SELECT
    p.product_id,
    COALESCE(pp.new_price, 10) AS price
FROM
    (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN ProductPrices pp
ON p.product_id = pp.product_id