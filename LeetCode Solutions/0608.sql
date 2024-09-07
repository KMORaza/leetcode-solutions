WITH ParentNodes AS (
    SELECT DISTINCT p_id
    FROM Tree
    WHERE p_id IS NOT NULL
),
NodeTypes AS (
    SELECT
        t.id,
        CASE
            WHEN t.p_id IS NULL THEN 'Root'
            WHEN t.id IN (SELECT p_id FROM ParentNodes) THEN 'Inner'
            ELSE 'Leaf'
        END AS type
    FROM Tree t
)
SELECT id, type
FROM NodeTypes;
