class Solution:
    def magicalString(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1
        s = [1, 2, 2]
        index = 2
        while len(s) < n:
            count = s[index]
            next_num = 1 if s[-1] == 2 else 2
            s.extend([next_num] * count)
            index += 1
        return s[:n].count(1)
