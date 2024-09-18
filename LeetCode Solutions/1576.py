class Solution:
    def modifyString(self, s: str) -> str:
        s_list = list(s)
        n = len(s_list)
        for i in range(n):
            if s_list[i] == '?':
                for char in 'abc':
                    if (i == 0 or s_list[i - 1] != char) and (i == n - 1 or s_list[i + 1] != char):
                        s_list[i] = char
                        break
        return ''.join(s_list)
