from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
def main():
    sol = Solution()
    print(sol.findContentChildren([1, 2, 3], [1, 1]))
    print(sol.findContentChildren([1, 2], [1, 2, 3]))
if __name__ == "__main__":
    main()
