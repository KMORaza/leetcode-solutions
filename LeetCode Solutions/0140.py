class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        def backtrack(start):
            if start in memo:
                return memo[start]
            result = []
            if start == len(s):
                return [""]
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    sub_sentences = backtrack(end)
                    for sentence in sub_sentences:
                        result.append((word + " " + sentence).strip())
            memo[start] = result
            return result
        return backtrack(0)