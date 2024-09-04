CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    SELECT salary
    FROM (
      SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
      FROM (SELECT DISTINCT salary FROM Employee) AS distinct_salaries
    ) AS ranked_salaries
    WHERE row_num = N
  );
END