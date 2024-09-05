WITH Unbanned_Users AS (
    SELECT users_id
    FROM Users
    WHERE banned = 'No'
),
Valid_Trips AS (
    SELECT t.id, t.client_id, t.driver_id, t.status, t.request_at
    FROM Trips t
    JOIN Unbanned_Users c ON t.client_id = c.users_id
    JOIN Unbanned_Users d ON t.driver_id = d.users_id
),
Daily_Stats AS (
    SELECT
        request_at AS Day,
        COUNT(*) AS total_requests,
        COUNT(CASE WHEN status IN ('cancelled_by_client', 'cancelled_by_driver') THEN 1 END) AS cancelled_requests
    FROM Valid_Trips
    WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY request_at
)
SELECT
    Day,
    ROUND(COALESCE(cancelled_requests * 1.0 / total_requests, 0), 2) AS `Cancellation Rate`
FROM Daily_Stats
ORDER BY Day;
