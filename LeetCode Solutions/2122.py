from collections import defaultdict
class Solution:
    def recoverArray(self, input_numbers):
        total_length = len(input_numbers)
        occurrence_map = defaultdict(int)
        for number in input_numbers:
            occurrence_map[number] += 1
        input_numbers.sort()
        for position in range(1, total_length):
            difference = input_numbers[position] - input_numbers[0]
            if difference <= 0 or difference % 2 == 1:
                continue
            occurrence_copy = occurrence_map.copy()
            reconstructed_array = self.construct_array(input_numbers, difference, occurrence_copy)
            if len(reconstructed_array) == total_length // 2:
                return reconstructed_array
        raise ValueError("Unable to recover a valid array.")
    def construct_array(self, input_numbers, difference, occurrence):
        new_array = []
        for number in input_numbers:
            if occurrence[number] == 0:
                continue
            if occurrence[number + difference] == 0:
                return []
            occurrence[number] -= 1
            occurrence[number + difference] -= 1
            new_array.append(number + difference // 2)
        return new_array
