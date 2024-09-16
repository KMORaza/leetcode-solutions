WITH Q1_Sales AS (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31'
),
Non_Q1_Sales AS (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
),
Products_Q1_Only AS (
    SELECT Q1.product_id
    FROM Q1_Sales Q1
    LEFT JOIN Non_Q1_Sales NonQ1
    ON Q1.product_id = NonQ1.product_id
    WHERE NonQ1.product_id IS NULL
)
SELECT P.product_id, P.product_name
FROM Products_Q1_Only PQ1
JOIN Product P
ON PQ1.product_id = P.product_id;
