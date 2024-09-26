from collections import Counter
from typing import List
class Solution:
    def recoverArray(self, size: int, total_sums: List[int]) -> List[int]:
        total_sums.sort()
        return self.find_elements(total_sums)
    def find_elements(self, total_sums: List[int]) -> List[int]:
        if len(total_sums) == 1:
            return []
        occurrences = Counter(total_sums)
        difference = total_sums[1] - total_sums[0]
        current_index = 0
        excluded_nums = [0] * (len(total_sums) // 2)
        included_nums = [0] * (len(total_sums) // 2)
        select_included_nums = False
        for current_sum in total_sums:
            if occurrences[current_sum] == 0:
                continue
            occurrences[current_sum] -= 1
            occurrences[current_sum + difference] -= 1
            excluded_nums[current_index] = current_sum
            included_nums[current_index] = current_sum + difference
            current_index += 1
            if current_sum + difference == 0:
                select_included_nums = True
        recovered_elements = self.find_elements(included_nums if select_included_nums else excluded_nums)
        recovered_elements.append(-difference if select_included_nums else difference)
        return recovered_elements
