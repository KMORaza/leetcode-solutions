class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_occurrence = {}
        current_day = 0

        for task in tasks:
            current_day += 1
            if task in last_occurrence:
                last_day = last_occurrence[task]
                earliest_day = last_day + space + 1
                if current_day < earliest_day:
                    current_day = earliest_day
            last_occurrence[task] = current_day

        return current_day