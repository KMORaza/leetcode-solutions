class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefixXOR = [0] * n
        prefixXOR[0] = arr[0]
        for i in range(1, n):
            prefixXOR[i] = prefixXOR[i - 1] ^ arr[i]
        results = []
        for left, right in queries:
            if left == 0:
                results.append(prefixXOR[right])
            else:
                results.append(prefixXOR[right] ^ prefixXOR[left - 1])
        return results
