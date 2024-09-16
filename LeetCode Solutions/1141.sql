WITH FilteredActivities AS (
    SELECT DISTINCT user_id, activity_date
    FROM Activity
    WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
),
DailyActiveUsers AS (
    SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
    FROM FilteredActivities
    GROUP BY activity_date
)
SELECT day, active_users
FROM DailyActiveUsers
ORDER BY day;