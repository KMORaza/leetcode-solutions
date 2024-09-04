WITH ConsecutiveLogs AS (
    SELECT L1.num AS num1, L2.num AS num2, L3.num AS num3
    FROM Logs L1
    JOIN Logs L2 ON L1.id = L2.id - 1 AND L1.num = L2.num
    JOIN Logs L3 ON L2.id = L3.id - 1 AND L2.num = L3.num
    WHERE L1.num = L3.num
)
SELECT DISTINCT num1 AS ConsecutiveNums
FROM ConsecutiveLogs;
