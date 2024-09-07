WITH FirstLogin AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),
ConsecutiveLogins AS (
    SELECT
        f.player_id
    FROM FirstLogin f
    JOIN Activity a
    ON f.player_id = a.player_id
    WHERE a.event_date = DATE_ADD(f.first_login_date, INTERVAL 1 DAY)
)
SELECT
    ROUND(
        COUNT(DISTINCT cl.player_id) / COUNT(DISTINCT fl.player_id),
        2
    ) AS fraction
FROM FirstLogin fl
LEFT JOIN ConsecutiveLogins cl
ON fl.player_id = cl.player_id;
