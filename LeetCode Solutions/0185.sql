WITH RankedSalaries AS (
    SELECT e.id,
           e.name,
           e.salary,
           e.departmentId,
           d.name AS departmentName,
           DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salaryRank
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)
SELECT departmentName AS Department,
       name AS Employee,
       salary AS Salary
FROM RankedSalaries
WHERE salaryRank <= 3
ORDER BY departmentName, Salary DESC;