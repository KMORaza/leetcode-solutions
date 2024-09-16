class Solution:
    def sampleStats(self, frequency):
        total_elements = sum(frequency)
        return [
            self.findLowest(frequency),
            self.findHighest(frequency),
            self.computeAverage(frequency, total_elements),
            (self.findLowerMedian(frequency, total_elements) + self.findUpperMedian(frequency, total_elements)) / 2.0,
            self.findMostFrequent(frequency)]
    def findLowest(self, frequency):
        for index in range(len(frequency)):
            if frequency[index] > 0:
                return index
        return -1
    def findHighest(self, frequency):
        for index in range(len(frequency) - 1, -1, -1):
            if frequency[index] > 0:
                return index
        return -1
    def computeAverage(self, frequency, total_elements):
        average_value = 0
        for index in range(len(frequency)):
            average_value += index * frequency[index] / total_elements
        return average_value
    def findLowerMedian(self, frequency, total_elements):
        accumulated_count = 0
        for index in range(len(frequency)):
            accumulated_count += frequency[index]
            if accumulated_count >= total_elements / 2:
                return index
        return -1
    def findUpperMedian(self, frequency, total_elements):
        accumulated_count = 0
        for index in range(len(frequency) - 1, -1, -1):
            accumulated_count += frequency[index]
            if accumulated_count >= total_elements / 2:
                return index
        return -1
    def findMostFrequent(self, frequency):
        most_frequent_value = -1
        max_frequency = 0
        for index in range(len(frequency)):
            if frequency[index] > max_frequency:
                max_frequency = frequency[index]
                most_frequent_value = index
        return most_frequent_value
