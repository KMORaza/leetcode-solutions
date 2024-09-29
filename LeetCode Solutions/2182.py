class Solution:
    def repeatLimitedString(self, input_str: str, limit: int) -> str:
        frequency_array = [0] * 26
        for char in input_str:
            frequency_array[ord(char) - ord('a')] += 1
        final_string_parts = []
        for char_index in range(25, -1, -1):
            smaller_char_index = char_index - 1
            while True:
                for _ in range(min(limit, frequency_array[char_index])):
                    frequency_array[char_index] -= 1
                    final_string_parts.append(chr(ord('a') + char_index))
                if frequency_array[char_index] == 0:
                    break
                while smaller_char_index >= 0 and frequency_array[smaller_char_index] == 0:
                    smaller_char_index -= 1
                if smaller_char_index < 0:
                    break
                frequency_array[smaller_char_index] -= 1
                final_string_parts.append(chr(ord('a') + smaller_char_index))
        return ''.join(final_string_parts)
