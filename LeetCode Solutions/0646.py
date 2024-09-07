from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        longest_chain_length = 0
        current_end = float('-inf')
        for pair in pairs:
            if pair[0] > current_end:
                longest_chain_length += 1
                current_end = pair[1]
        return longest_chain_length
