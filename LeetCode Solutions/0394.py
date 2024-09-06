class Solution:
    def decodeString(self, s: str) -> str:
        char_stack = []
        num_stack = []
        current_num = 0
        current_str = ''
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                num_stack.append(current_num)
                char_stack.append(current_str)
                current_str = ''
                current_num = 0
            elif char == ']':
                prev_str = char_stack.pop()
                repeat_num = num_stack.pop()
                current_str = prev_str + current_str * repeat_num
            else:
                current_str += char
        return current_str
