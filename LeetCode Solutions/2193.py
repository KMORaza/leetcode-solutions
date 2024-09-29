class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        s = list(s)
        left = 0
        right = n - 1
        moves = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                k = right
                while k > left and s[k] != s[left]:
                    k -= 1
                if k == left:
                    s[left], s[left + 1] = s[left + 1], s[left]
                    moves += 1
                else:
                    while k < right:
                        s[k], s[k + 1] = s[k + 1], s[k]
                        k += 1
                        moves += 1
                    left += 1
                    right -= 1
        return moves
