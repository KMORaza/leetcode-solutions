from collections import defaultdict
class Solution:
    X = 1000000007
    def threeSumMulti(self, numbers, target_sum):
        frequency = defaultdict(int)
        for num in numbers:
            frequency[num] += 1
        result = 0
        for current_index in range(len(numbers)):
            middle = numbers[current_index]
            frequency[middle] -= 1
            for prev_index in range(current_index):
                first = numbers[prev_index]
                third = target_sum - first - middle
                if third in frequency:
                    result = (result + frequency[third]) % self.X
        return int(result)
