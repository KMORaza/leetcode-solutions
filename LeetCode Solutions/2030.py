class Solution:
    def smallestSubsequence(self, input_string: str, target_length: int, target_char: str, min_repeats: int) -> str:
        char_stack = []
        required_repeats = min_repeats
        total_target_chars = input_string.count(target_char)
        for index, current_char in enumerate(input_string):
            while (char_stack and
                   char_stack[-1] > current_char and
                   len(char_stack) + len(input_string) - index - 1 >= target_length and
                   (char_stack[-1] != target_char or total_target_chars > required_repeats)):
                if char_stack.pop() == target_char:
                    required_repeats += 1
            if len(char_stack) < target_length:
                if current_char == target_char:
                    char_stack.append(current_char)
                    required_repeats -= 1
                elif target_length - len(char_stack) > required_repeats:
                    char_stack.append(current_char)
            if current_char == target_char:
                total_target_chars -= 1
        return ''.join(char_stack[:target_length])

