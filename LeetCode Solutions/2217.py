from typing import List
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        results = []
        if intLength % 2 == 0:
            half_length = intLength // 2
            start = 10**(half_length - 1)
            end = 10**half_length
        else:
            half_length = intLength // 2 + 1
            start = 10**(half_length - 1)
            end = 10**half_length
        for k in queries:
            first_half = start + k - 1
            if first_half >= end:
                results.append(-1)
            else:
                if intLength % 2 == 0:
                    first_half_str = str(first_half)
                    palindrome = int(first_half_str + first_half_str[::-1])
                else:
                    first_half_str = str(first_half)
                    palindrome = int(first_half_str + first_half_str[-2::-1])
                results.append(palindrome)
        return results
