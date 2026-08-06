class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = [0, 0, 0]

        for c in s:
            count[ord(c) - ord('a')] += 1

        if count[0] < k or count[1] < k or count[2] < k:
            return -1

        max_window = 0
        left = 0

        for right in range(n):
            count[ord(s[right]) - ord('a')] -= 1

            while count[0] < k or count[1] < k or count[2] < k:
                count[ord(s[left]) - ord('a')] += 1
                left += 1

            max_window = max(max_window, right - left + 1)

        return n - max_window