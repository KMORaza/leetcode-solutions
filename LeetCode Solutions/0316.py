class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = {char: 0 for char in s}
        for char in s:
            freq[char] += 1
        stack = []
        in_stack = {char: False for char in s}
        for char in s:
            freq[char] -= 1
            if in_stack[char]:
                continue
            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                removed_char = stack.pop()
                in_stack[removed_char] = False
            stack.append(char)
            in_stack[char] = True
        return ''.join(stack)
