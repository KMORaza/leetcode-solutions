class Solution:
    def minSwap(self, x1: list[int], x2: list[int]) -> int:
        not_swapped_last, swapped_last = 0, 1
        for i in range(1, len(x1)):
            prev_not_swapped_last, prev_swapped_last = not_swapped_last, swapped_last
            not_swapped_last = swapped_last = len(x1)
            if x1[i - 1] < x1[i] and x2[i - 1] < x2[i]:
                not_swapped_last = prev_not_swapped_last
                swapped_last = prev_swapped_last + 1
            if x1[i - 1] < x2[i] and x2[i - 1] < x1[i]:
                not_swapped_last = min(not_swapped_last, prev_swapped_last)
                swapped_last = min(swapped_last, prev_not_swapped_last + 1)
        return min(not_swapped_last, swapped_last)
