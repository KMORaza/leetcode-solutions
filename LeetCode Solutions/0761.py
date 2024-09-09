class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def process(s: str) -> str:
            count = i = 0
            result = []
            for j, char in enumerate(s):
                count += 1 if char == '1' else -1
                if count == 0:
                    result.append('1' + process(s[i + 1:j]) + '0')
                    i = j + 1
            return ''.join(sorted(result, reverse=True))
        return process(s)
