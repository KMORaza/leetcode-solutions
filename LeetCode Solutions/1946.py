from typing import List
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num_list = list(num)
        made_change = False
        for i in range(len(num_list)):
            digit = int(num_list[i])
            if change[digit] > digit:
                num_list[i] = str(change[digit])
                made_change = True
            elif made_change:
                if change[digit] < digit:
                    break
        return ''.join(num_list)