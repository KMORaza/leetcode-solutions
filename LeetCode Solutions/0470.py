class Solution:
    def rand10(self) -> int:
        while True:
            row = rand7()
            col = rand7()
            num = (row - 1) * 7 + col
            if num <= 40:
                return (num - 1) % 10 + 1
