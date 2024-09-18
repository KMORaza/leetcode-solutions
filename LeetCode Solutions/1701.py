from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        current_time = 0
        for arrival, duration in customers:
            if current_time < arrival:
                current_time = arrival
            current_time += duration
            total_waiting_time += current_time - arrival
        return total_waiting_time / len(customers)
