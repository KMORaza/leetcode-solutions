from collections import deque
class Solution:
    def maxTaskAssign(self, job_durations, employee_capacities, available_pills, boost_strength):
        job_durations.sort()
        employee_capacities.sort()
        self.job_durations = job_durations
        self.employee_capacities = employee_capacities
        self.boost_strength = boost_strength
        self.available_pills = available_pills
        total_jobs = len(job_durations)
        total_employees = len(employee_capacities)
        lower_bound, upper_bound = 0, min(total_employees, total_jobs)
        while lower_bound < upper_bound:
            midpoint = (lower_bound + upper_bound + 1) // 2
            if self.can_assign(midpoint, total_jobs, total_employees):
                lower_bound = midpoint
            else:
                upper_bound = midpoint - 1
        return lower_bound
    def can_assign(self, num_jobs_to_assign, total_jobs, total_employees):
        job_pointer = 0
        job_queue = deque()
        remaining_pills = self.available_pills
        for emp_index in range(total_employees - num_jobs_to_assign, total_employees):
            while job_pointer < num_jobs_to_assign and self.job_durations[job_pointer] <= self.employee_capacities[emp_index] + self.boost_strength:
                job_queue.append(self.job_durations[job_pointer])
                job_pointer += 1
            if not job_queue:
                return False
            if job_queue[0] <= self.employee_capacities[emp_index]:
                job_queue.popleft()
            elif remaining_pills == 0:
                return False
            else:
                remaining_pills -= 1
                job_queue.pop()
        return True