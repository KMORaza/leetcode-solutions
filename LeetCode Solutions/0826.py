from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        max_difficulty = max(difficulty)
        max_profit_up_to_difficulty = [0] * (max_difficulty + 1)
        current_max_profit = 0
        job_index = 0
        for i in range(1, max_difficulty + 1):
            while job_index < len(jobs) and jobs[job_index][0] <= i:
                current_max_profit = max(current_max_profit, jobs[job_index][1])
                job_index += 1
            max_profit_up_to_difficulty[i] = current_max_profit
        total_profit = 0
        for ability in worker:
            if ability > 0:
                if ability > max_difficulty:
                    total_profit += max_profit_up_to_difficulty[max_difficulty]
                else:
                    total_profit += max_profit_up_to_difficulty[ability]
        return total_profit
