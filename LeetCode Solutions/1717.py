class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            first, second, first_score, second_score = "ba", "ab", y, x
        else:
            first, second, first_score, second_score = "ab", "ba", x, y
        total_gain = 0
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 2 and ''.join(stack[-2:]) == first:
                stack.pop()
                stack.pop()
                total_gain += first_score
        s = ''.join(stack)
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 2 and ''.join(stack[-2:]) == second:
                stack.pop()
                stack.pop()
                total_gain += second_score
        return total_gain
