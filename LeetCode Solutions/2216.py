class Solution:
    def minDeletion(self, sequence):
        removal_count = 0
        for current_index in range(len(sequence) - 1):
            if sequence[current_index] == sequence[current_index + 1] and (current_index - removal_count) % 2 == 0:
                removal_count += 1
        return removal_count + (1 if (len(sequence) - removal_count) % 2 == 1 else 0)