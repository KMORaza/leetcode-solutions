from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        max_chain_length = 1
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            max_chain_length = max(max_chain_length, dp[word])
        return max_chain_length
