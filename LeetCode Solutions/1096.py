class Solution:
    def __init__(self):
        self.set_output = set()
    def braceExpansionII(self, expression: str) -> list[str]:
        self._depth_first_search(expression)
        return sorted(self.set_output)
    def _depth_first_search(self, exp: str):
        close = exp.find('}')
        if close == -1:
            self.set_output.add(exp)
            return
        open = exp.rfind('{', 0, close)
        before_braces = exp[:open]
        after_braces = exp[close + 1:]
        for inside_braces in exp[open + 1:close].split(','):
            self._depth_first_search(before_braces + inside_braces + after_braces)
if __name__ == "__main__":
    solution = Solution()
    results = solution.braceExpansionII("{a,b}c{d,e}f")
    for result in results:
        print(result)
