from functools import lru_cache
x = 1000000007
class Solution:
    def findGoodStrings(self, length: int, lowerBound: str, upperBound: str, forbidden: str) -> int:
        lowerBound = list(map(ord, lowerBound))
        upperBound = list(map(ord, upperBound))
        forbidden = list(map(ord, forbidden))
        f_len = len(forbidden)
        prefix_function = [0] * f_len
        powers_of_26 = [0] * (length + 1)
        current_length = 0
        index = 1
        while index < f_len:
            if forbidden[index] == forbidden[current_length]:
                current_length += 1
                prefix_function[index] = current_length
                index += 1
            elif current_length > 0:
                current_length = prefix_function[current_length - 1]
            else:
                prefix_function[index] = 0
                index += 1
        powers_of_26[0] = 1
        for index in range(1, length + 1):
            powers_of_26[index] = (26 * powers_of_26[index - 1]) % x
        @lru_cache(None)
        def count_valid_strings(pos: int, match_length: int, lower_bound_active: int, upper_bound_active: int) -> int:
            if match_length == f_len:
                return 0
            if pos == length:
                return 1
            min_char = lowerBound[pos] - ord('a') if lower_bound_active > 0 else 0
            max_char = upperBound[pos] - ord('a') if upper_bound_active > 0 else 25
            result = 0
            for char in range(min_char, max_char + 1):
                next_pos = pos + 1
                next_match_length = match_length
                while next_match_length > 0 and forbidden[next_match_length] != char + ord('a'):
                    next_match_length = prefix_function[next_match_length - 1]
                if char == forbidden[next_match_length] - ord('a'):
                    next_match_length += 1
                result = (result + count_valid_strings(next_pos, next_match_length, lower_bound_active & (char == min_char), upper_bound_active & (char == max_char))) % x
            return result
        return count_valid_strings(0, 0, 1, 1)
