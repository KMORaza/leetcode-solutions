class Solution:
    def minOperations(self, numbers):
        size = len(numbers)
        result = size
        unique_numbers = sorted(set(numbers))
        for pos in range(len(unique_numbers)):
            initial = unique_numbers[pos]
            boundary = initial + size - 1
            next_index = self.locateFirstExceeding(unique_numbers, boundary)
            distinct_count = next_index - pos
            result = min(result, size - distinct_count)
        return result
    def locateFirstExceeding(self, collection, threshold):
        start, end = 0, len(collection)
        while start < end:
            mid_point = (start + end) // 2
            if collection[mid_point] <= threshold:
                start = mid_point + 1
            else:
                end = mid_point
        return start
