WITH OrderedQueue AS (
    SELECT
        person_name,
        weight,
        ROW_NUMBER() OVER (ORDER BY turn) AS row_num
    FROM
        Queue
),
CumulativeWeights AS (
    SELECT
        person_name,
        weight,
        row_num,
        SUM(weight) OVER (ORDER BY row_num ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_weight
    FROM
        OrderedQueue
)
SELECT
    person_name
FROM
    CumulativeWeights
WHERE
    total_weight <= 1000
ORDER BY
    row_num DESC
LIMIT 1;
