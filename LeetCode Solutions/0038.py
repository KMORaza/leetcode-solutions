class Solution:
    def countAndSay(self, n: int) -> str:
        def encode(s: str) -> str:
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count))
                result.append(s[i])
                i += 1
            return ''.join(result)
        current = "1"
        for _ in range(1, n):
            current = encode(current)
        return current