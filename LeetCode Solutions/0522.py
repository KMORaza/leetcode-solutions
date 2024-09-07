class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(small: str, large: str) -> bool:
            it = iter(large)
            return all(char in it for char in small)
        max_length = -1
        for i, str1 in enumerate(strs):
            uncommon = True
            for j, str2 in enumerate(strs):
                if i != j and is_subsequence(str1, str2):
                    uncommon = False
                    break
            if uncommon:
                max_length = max(max_length, len(str1))
        return max_length
