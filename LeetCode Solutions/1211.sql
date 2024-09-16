WITH Quality AS (
    SELECT
        query_name,
        AVG(rating * 1.0 / position) AS quality
    FROM Queries
    GROUP BY query_name
),
PoorQuery AS (
    SELECT
        query_name,
        SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) AS poor_query_count,
        COUNT(*) AS total_query_count
    FROM Queries
    GROUP BY query_name
),
PoorQueryPercentage AS (
    SELECT
        query_name,
        (poor_query_count * 1.0 / total_query_count) * 100 AS poor_query_percentage
    FROM PoorQuery
)
SELECT
    q.query_name,
    ROUND(q.quality, 2) AS quality,
    ROUND(p.poor_query_percentage, 2) AS poor_query_percentage
FROM Quality q
JOIN PoorQueryPercentage p ON q.query_name = p.query_name;
