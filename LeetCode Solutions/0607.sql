WITH RedCompany AS (
    SELECT com_id
    FROM Company
    WHERE name = 'RED'
),
SalesWithRedOrders AS (
    SELECT DISTINCT sales_id
    FROM Orders
    JOIN RedCompany ON Orders.com_id = RedCompany.com_id
),
SalespersonsWithoutRedOrders AS (
    SELECT name
    FROM SalesPerson
    WHERE sales_id NOT IN (SELECT sales_id FROM SalesWithRedOrders)
)
SELECT name
FROM SalespersonsWithoutRedOrders;
