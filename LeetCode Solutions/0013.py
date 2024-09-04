class Solution:
    def romanToInt(self, s):
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        length = len(s)
        for i in range(length):
            current_value = roman_to_int[s[i]]
            if i + 1 < length and roman_to_int[s[i + 1]] > current_value:
                total -= current_value
            else:
                total += current_value
        return total
