WITH ConsecutiveGroups AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
GroupCounts AS (
    SELECT
        grp,
        COUNT(*) AS cnt
    FROM ConsecutiveGroups
    GROUP BY grp
    HAVING COUNT(*) >= 3
),
FinalResults AS (
    SELECT
        c.id,
        c.visit_date,
        c.people
    FROM ConsecutiveGroups c
    JOIN GroupCounts g ON c.grp = g.grp
)
SELECT
    id,
    visit_date,
    people
FROM FinalResults
ORDER BY visit_date;
