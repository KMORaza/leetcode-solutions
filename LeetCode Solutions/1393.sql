
WITH RankedOperations AS (
    SELECT
        stock_name,
        operation,
        operation_day,
        price,
        ROW_NUMBER() OVER (PARTITION BY stock_name, operation ORDER BY operation_day) AS rn
    FROM Stocks
),
PairedTransactions AS (
    SELECT
        b.stock_name,
        b.operation_day AS buy_day,
        s.operation_day AS sell_day,
        s.price AS sell_price,
        b.price AS buy_price
    FROM
        RankedOperations b
    JOIN
        RankedOperations s
    ON
        b.stock_name = s.stock_name
    AND
        b.rn = s.rn
    AND
        b.operation = 'Buy'
    AND
        s.operation = 'Sell'
    AND
        b.operation_day < s.operation_day
),
CapitalGains AS (
    SELECT
        stock_name,
        SUM(sell_price - buy_price) AS capital_gain_loss
    FROM
        PairedTransactions
    GROUP BY
        stock_name
)
SELECT
    stock_name,
    capital_gain_loss
FROM
    CapitalGains;
