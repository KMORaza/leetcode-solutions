class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        from collections import deque

        n = len(chargeTimes)
        max_deque = deque()
        left = 0
        total_running_cost = 0
        max_robots = 0

        for right in range(n):
            while max_deque and chargeTimes[max_deque[-1]] <= chargeTimes[right]:
                max_deque.pop()
            max_deque.append(right)

            total_running_cost += runningCosts[right]

            while left <= right:
                max_charge = chargeTimes[max_deque[0]]
                k = right - left + 1
                total_cost = max_charge + k * total_running_cost

                if total_cost <= budget:
                    max_robots = max(max_robots, k)
                    break
                else:
                    total_running_cost -= runningCosts[left]
                    if max_deque[0] == left:
                        max_deque.popleft()
                    left += 1

        return max_robots