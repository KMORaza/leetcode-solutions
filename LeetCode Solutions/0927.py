class Solution:
    def threeEqualParts(self, arr):
        binary_array = arr
        count_of_ones = 0
        array_length = len(arr)
        for value in arr:
            count_of_ones += value
        if count_of_ones % 3 != 0:
            return [-1, -1]
        if count_of_ones == 0:
            return [0, array_length - 1]
        count_of_ones //= 3
        first = self.findNthOne(binary_array, 1)
        second = self.findNthOne(binary_array, count_of_ones + 1)
        third = self.findNthOne(binary_array, 2 * count_of_ones + 1)
        while third < array_length and \
              binary_array[first] == binary_array[second] and \
              binary_array[second] == binary_array[third]:
            first += 1
            second += 1
            third += 1
        return [first - 1, second] if third == array_length else [-1, -1]
    def findNthOne(self, binary_array, nth_one):
        sum_ones = 0
        for i in range(len(binary_array)):
            sum_ones += binary_array[i]
            if sum_ones == nth_one:
                return i
        return -1