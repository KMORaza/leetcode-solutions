class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box_count = {}
        for num in range(lowLimit, highLimit + 1):
            box_number = sum(int(digit) for digit in str(num))
            if box_number in box_count:
                box_count[box_number] += 1
            else:
                box_count[box_number] = 1
        return max(box_count.values())
