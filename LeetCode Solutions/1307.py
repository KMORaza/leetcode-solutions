from itertools import permutations
class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        def convert_to_number(word: str, letter_to_digit: dict) -> int:
            return int(''.join(str(letter_to_digit[char]) for char in word))

        def check_mapping(letter_to_digit: dict) -> bool:
            for word in words + [result]:
                if letter_to_digit[word[0]] == 0 and len(word) > 1:
                    return False
            total = sum(convert_to_number(word, letter_to_digit) for word in words)
            return total == convert_to_number(result, letter_to_digit)

        unique_chars = set(''.join(words) + result)
        if len(unique_chars) > 10:
            return False
        letter_list = list(unique_chars)
        for digit_perm in permutations(range(10), len(letter_list)):
            letter_to_digit_map = dict(zip(letter_list, digit_perm))
            if check_mapping(letter_to_digit_map):
                return True
        return False
