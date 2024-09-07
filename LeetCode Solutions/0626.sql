SELECT
    s1.id AS id,
    COALESCE(s2.student, s1.student) AS student
FROM Seat s1
LEFT JOIN Seat s2
ON s1.id = s2.id - 1
WHERE s1.id % 2 = 1
UNION ALL
SELECT
    s2.id AS id,
    s1.student AS student
FROM Seat s1
JOIN Seat s2
ON s1.id = s2.id - 1
WHERE s1.id % 2 = 1
ORDER BY id;