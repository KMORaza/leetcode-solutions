from typing import List
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def canDistribute(jobs, k, maxTime):
            def backtrack(i, worker_times):
                if i == len(jobs):
                    return True
                for j in range(k):
                    if worker_times[j] + jobs[i] <= maxTime:
                        worker_times[j] += jobs[i]
                        if backtrack(i + 1, worker_times):
                            return True
                        worker_times[j] -= jobs[i]
                    if worker_times[j] == 0:
                        break
                return False
            worker_times = [0] * k
            return backtrack(0, worker_times)
        low, high = max(jobs), sum(jobs)
        while low < high:
            mid = (low + high) // 2
            if canDistribute(jobs, k, mid):
                high = mid
            else:
                low = mid + 1
        return low
