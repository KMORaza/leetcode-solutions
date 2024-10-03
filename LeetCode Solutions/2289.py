class Solution:
    def totalSteps(self, sequence):
        index_tracker = []
        overall_steps = 0
        seq_length = len(sequence)
        endurance_rounds = [0] * seq_length
        for position in range(seq_length - 1, -1, -1):
            while index_tracker and sequence[position] > sequence[index_tracker[-1]]:
                endurance_rounds[position] = max(endurance_rounds[position] + 1, endurance_rounds[index_tracker.pop()])
                overall_steps = max(overall_steps, endurance_rounds[position])
            index_tracker.append(position)
        return overall_steps