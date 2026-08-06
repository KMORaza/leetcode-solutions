class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = list(str(num))

        mx = s[:]
        for c in mx:
            if c != '9':
                d = c
                mx = ['9' if x == d else x for x in mx]
                break

        mn = s[:]
        d = mn[0]
        mn = ['0' if x == d else x for x in mn]

        return int(''.join(mx)) - int(''.join(mn))