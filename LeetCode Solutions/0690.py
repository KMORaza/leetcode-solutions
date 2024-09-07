class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        employee_map = {employee.id: (employee.importance, employee.subordinates) for employee in employees}
        def dfs(emp_id):
            if emp_id not in employee_map:
                return 0
            importance, subordinates = employee_map[emp_id]
            total_importance = importance
            for sub_id in subordinates:
                total_importance += dfs(sub_id)
            return total_importance
        return dfs(id)
