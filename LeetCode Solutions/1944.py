class Solution:
    def canSeePersonsCount(self, altitude):
        total = len(altitude)
        visibility_count = [0] * total
        position_stack = []
        for position in range(total):
            while position_stack and altitude[position_stack[-1]] <= altitude[position]:
                visibility_count[position_stack.pop()] += 1
            if position_stack:
                visibility_count[position_stack[-1]] += 1
            position_stack.append(position)
        return visibility_count