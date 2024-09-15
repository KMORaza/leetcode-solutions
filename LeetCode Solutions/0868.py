class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        max_gap = 0
        last_index = -1
        for index, char in enumerate(binary):
            if char == '1':
                if last_index != -1:
                    max_gap = max(max_gap, index - last_index)
                last_index = index
        return max_gap
