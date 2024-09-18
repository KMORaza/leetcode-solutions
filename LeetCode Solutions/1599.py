from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        max_operations = -1
        total_customers = 0
        current_profit = 0
        total_operations = 0
        queue_index = 0
        while queue_index < len(customers) or total_customers > 0:
            if queue_index < len(customers):
                total_customers += customers[queue_index]
                queue_index += 1
            if total_customers > 4:
                boarded = 4
            else:
                boarded = total_customers
            current_profit += boarded * boardingCost - runningCost
            total_customers -= boarded
            total_operations += 1
            if current_profit > max_profit:
                max_profit = current_profit
                max_operations = total_operations
        return max_operations if max_profit > 0 else -1
