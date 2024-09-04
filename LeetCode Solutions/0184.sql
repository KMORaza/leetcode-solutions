WITH MaxSalaryPerDepartment AS (
    SELECT departmentId,
           MAX(salary) AS maxSalary
    FROM Employee
    GROUP BY departmentId
)
SELECT D.name AS Department,
       E.name AS Employee,
       E.salary AS Salary
FROM Employee E
JOIN MaxSalaryPerDepartment MS ON E.departmentId = MS.departmentId AND E.salary = MS.maxSalary
JOIN Department D ON E.departmentId = D.id;
