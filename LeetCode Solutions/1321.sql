WITH daily_amounts AS (
    SELECT
        visited_on,
        SUM(amount) AS total_amount
    FROM
        customer
    GROUP BY
        visited_on
),
week_sum AS (
    SELECT
        da1.visited_on,
        da1.total_amount AS daily_amount,
        COALESCE(SUM(da2.total_amount), 0) AS rolling_sum
    FROM
        daily_amounts da1
    LEFT JOIN
        daily_amounts da2
    ON
        da2.visited_on BETWEEN da1.visited_on - INTERVAL 6 DAY AND da1.visited_on
    GROUP BY
        da1.visited_on, da1.total_amount
),
average_amounts AS (
    SELECT
        visited_on,
        rolling_sum,
        ROUND(rolling_sum / 7, 2) AS average_amount
    FROM
        week_sum
)
SELECT
    visited_on,
    rolling_sum AS amount,
    average_amount
FROM
    average_amounts
WHERE
    visited_on >= (SELECT MIN(visited_on) FROM daily_amounts) + INTERVAL 6 DAY
ORDER BY
    visited_on;
