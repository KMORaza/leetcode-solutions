class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        even_digits = sorted((d for d in digits if d % 2 == 0), reverse=True)
        odd_digits = sorted((d for d in digits if d % 2 != 0), reverse=True)
        result = []
        even_index = 0
        odd_index = 0
        for d in digits:
            if d % 2 == 0:
                result.append(even_digits[even_index])
                even_index += 1
            else:
                result.append(odd_digits[odd_index])
                odd_index += 1
        return int(''.join(map(str, result)))
