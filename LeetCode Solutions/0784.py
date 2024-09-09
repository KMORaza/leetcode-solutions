from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(index: int, path: List[str]):
            if index == len(s):
                result.append("".join(path))
                return
            char = s[index]
            if char.isalpha():
                path.append(char.lower())
                backtrack(index + 1, path)
                path[-1] = char.upper()
                backtrack(index + 1, path)
                path.pop()
            else:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()
        result = []
        backtrack(0, [])
        return result
