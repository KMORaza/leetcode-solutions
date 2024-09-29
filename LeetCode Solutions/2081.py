class Solution:
    def kMirror(self, numeral_base: int, target_count: int) -> int:
        total_kmirror_sum = 0
        palindrome_length = 1
        while True:
            min_prefix = 10 ** ((palindrome_length - 1) // 2)
            max_prefix = 10 ** ((palindrome_length + 1) // 2)
            for prefix_value in range(min_prefix, max_prefix):
                constructed_palindrome = prefix_value
                if palindrome_length % 2 == 0:
                    mirror_part = prefix_value
                else:
                    mirror_part = prefix_value // 10
                while mirror_part > 0:
                    constructed_palindrome = constructed_palindrome * 10 + mirror_part % 10
                    mirror_part //= 10
                base_representation_string = self.convert_to_base(constructed_palindrome, numeral_base)
                if self.check_palindrome(base_representation_string):
                    total_kmirror_sum += constructed_palindrome
                    target_count -= 1
                    if target_count == 0:
                        return total_kmirror_sum
            palindrome_length += 1
    def check_palindrome(self, string_input: str) -> bool:
        return string_input == string_input[::-1]
    def convert_to_base(self, number_value: int, base_value: int) -> str:
        if number_value == 0:
            return '0'
        digit_list = []
        while number_value:
            digit_list.append(str(number_value % base_value))
            number_value //= base_value
        return ''.join(digit_list[::-1])
