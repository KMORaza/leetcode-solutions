class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def count_happy_strings(length: int, last_char: str) -> int:
            if length == 0:
                return 1
            if (length, last_char) in memo:
                return memo[(length, last_char)]
            total = 0
            for char in 'abc':
                if char != last_char:
                    total += count_happy_strings(length - 1, char)
            memo[(length, last_char)] = total
            return total
        memo = {}
        total_count = count_happy_strings(n, '')
        if k > total_count:
            return ''
        result = []
        prev_char = ''
        current_k = k
        for i in range(n):
            for char in 'abc':
                if char != prev_char:
                    count = count_happy_strings(n - i - 1, char)
                    if current_k <= count:
                        result.append(char)
                        prev_char = char
                        break
                    current_k -= count
        return ''.join(result)
