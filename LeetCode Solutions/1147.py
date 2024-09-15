class Solution:
    def longestDecomposition(self, text: str) -> int:
        count = 0
        start, end = 0, len(text) - 1
        while start <= end:
            found_matching_part = False
            for k in range(1, (end - start + 1) // 2 + 1):
                if self.is_matching_part(text, start, end - k + 1, k):
                    count += 2
                    start += k
                    end -= k
                    found_matching_part = True
                    break
            if not found_matching_part:
                count += 1
                break
        return count
    def is_matching_part(self, s: str, start: int, end: int, k: int) -> bool:
        return s[start:start + k] == s[end:end + k]
