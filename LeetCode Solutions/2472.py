class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1:
            return n

        def expand_around_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    return left, right
                left -= 1
                right += 1
            return -1, -1

        intervals = []
        for i in range(n):
            l1, r1 = expand_around_center(i, i)
            if l1 != -1:
                intervals.append((l1, r1))
            l2, r2 = expand_around_center(i, i + 1)
            if l2 != -1:
                intervals.append((l2, r2))

        intervals.sort(key=lambda x: x[1])

        count = 0
        last_end = -1

        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end

        return count