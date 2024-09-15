from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(sublist: List[int], k: int) -> None:
            left, right = 0, k
            while left < right:
                sublist[left], sublist[right] = sublist[right], sublist[left]
                left += 1
                right -= 1
        def find_max_index(sublist: List[int], n: int) -> int:
            max_index = 0
            for i in range(1, n):
                if sublist[i] > sublist[max_index]:
                    max_index = i
            return max_index
        result = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_index = find_max_index(arr, size)
            if max_index + 1 != size:
                if max_index != 0:
                    result.append(max_index + 1)
                    flip(arr, max_index)
                result.append(size)
                flip(arr, size - 1)
        return result
