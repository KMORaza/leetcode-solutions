WITH UserCount AS (
    SELECT COUNT(DISTINCT user_id) AS total_users
    FROM Users
),
ContestRegistration AS (
    SELECT
        contest_id,
        COUNT(DISTINCT user_id) AS registered_users
    FROM
        Register
    GROUP BY
        contest_id
)
SELECT
    cr.contest_id,
    ROUND((cr.registered_users * 100.0 / uc.total_users), 2) AS percentage
FROM
    ContestRegistration cr
JOIN
    UserCount uc ON 1 = 1
ORDER BY
    percentage DESC,
    cr.contest_id ASC;
