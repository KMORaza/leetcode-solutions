class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        total_cost = 0
        max_length = 0
        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            total_cost += cost
            while total_cost > maxCost:
                total_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
