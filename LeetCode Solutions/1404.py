class Solution:
    def numSteps(self, input_str: str) -> int:
        step_count = 0
        char_list = list(input_str)
        while char_list and char_list[-1] == '0':
            char_list.pop()
            step_count += 1
        if ''.join(char_list) == "1":
            return step_count
        step_count += 1
        for char in char_list:
            step_count += 1 if char == '1' else 2
        return step_count