class Solution:
    def rearrangeArray(self, input_array):
        input_array.sort()
        for index in range(1, len(input_array), 2):
            input_array[index], input_array[index - 1] = input_array[index - 1], input_array[index]
        return input_array
