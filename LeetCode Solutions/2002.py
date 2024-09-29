class Solution:
    def maxProduct(self, input_string: str) -> int:
        self.maximum_product = 0
        self.explore_combinations(input_string, 0, [], [])
        return self.maximum_product
    def explore_combinations(self, input_string: str, current_index: int, first_part: list, second_part: list):
        if current_index == len(input_string):
            if self.is_valid_palindrome(first_part) and self.is_valid_palindrome(second_part):
                self.maximum_product = max(self.maximum_product, len(first_part) * len(second_part))
            return
        first_part.append(input_string[current_index])
        self.explore_combinations(input_string, current_index + 1, first_part, second_part)
        first_part.pop()
        second_part.append(input_string[current_index])
        self.explore_combinations(input_string, current_index + 1, first_part, second_part)
        second_part.pop()
        self.explore_combinations(input_string, current_index + 1, first_part, second_part)
    def is_valid_palindrome(self, substring_list: list) -> bool:
        return substring_list == substring_list[::-1]
