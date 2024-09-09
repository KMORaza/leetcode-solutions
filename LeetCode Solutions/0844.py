class Solution:
    @staticmethod
    def backspaceCompare(s: str, t: str) -> bool:
        def build(final_str: str) -> str:
            result = []
            for char in final_str:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return ''.join(result)
        return build(s) == build(t)
