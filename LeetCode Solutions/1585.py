from collections import deque
class Solution:
    def isTransformable(self, source: str, target: str) -> bool:
        def count_digits(s: str) -> list[int]:
            digit_count = [0] * 10
            for char in s:
                digit_count[int(char)] += 1
            return digit_count
        if count_digits(source) != count_digits(target):
            return False
        digit_positions = [deque() for _ in range(10)]
        for index, char in enumerate(source):
            digit_positions[int(char)].append(index)
        for char in target:
            digit = int(char)
            position = digit_positions[digit].popleft()
            for smaller_digit in range(digit):
                if digit_positions[smaller_digit] and digit_positions[smaller_digit][0] < position:
                    return False
        return True
