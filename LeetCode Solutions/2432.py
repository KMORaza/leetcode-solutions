class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = logs[0][1]
        emp_id = logs[0][0]
        prev_time = 0

        for eid, time in logs:
            duration = time - prev_time
            if duration > max_time or (duration == max_time and eid < emp_id):
                max_time = duration
                emp_id = eid
            prev_time = time

        return emp_id