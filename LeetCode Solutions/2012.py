class Solution:
    def sumOfBeauties(self, values):
        length = len(values)
        beauty_sum = 0
        right_min = [0] * length
        right_min[length - 1] = values[length - 1]
        for index in range(length - 2, 1, -1):
            right_min[index] = min(values[index], right_min[index + 1])
        left_max = values[0]
        for index in range(1, length - 1):
            if left_max < values[index] < right_min[index + 1]:
                beauty_sum += 2
            elif values[index - 1] < values[index] < values[index + 1]:
                beauty_sum += 1
            left_max = max(left_max, values[index])
        return beauty_sum
