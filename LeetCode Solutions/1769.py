class Solution:
    def minOperations(self, container: str) -> list[int]:
        length = len(container)
        results = [0] * length
        counter = 0
        total_moves = 0
        for index in range(length):
            results[index] += total_moves
            counter += 1 if container[index] == '1' else 0
            total_moves += counter
        counter = 0
        total_moves = 0
        for index in range(length - 1, -1, -1):
            results[index] += total_moves
            counter += 1 if container[index] == '1' else 0
            total_moves += counter
        return results

