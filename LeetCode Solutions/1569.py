from typing import List
class Solution:
    X = 1000000007
    def numOfWays(self, arr: List[int]) -> int:
        self.combinations_matrix = self._generate_combinations(len(arr) + 1)
        return self._calculate_ways(arr) - 1
    def _calculate_ways(self, arr: List[int]) -> int:
        if len(arr) <= 2:
            return 1
        root = arr[0]
        left_subtree = [x for x in arr[1:] if x < root]
        right_subtree = [x for x in arr[1:] if x >= root]
        num_ways = self.combinations_matrix[len(arr) - 1][len(left_subtree)]
        num_ways = (num_ways * self._calculate_ways(left_subtree)) % self.X
        num_ways = (num_ways * self._calculate_ways(right_subtree)) % self.X
        return num_ways
    def _generate_combinations(self, num_rows: int) -> List[List[int]]:
        combinations_matrix = [[1] * (i + 1) for i in range(num_rows)]
        for i in range(2, num_rows):
            for j in range(1, len(combinations_matrix[i]) - 1):
                combinations_matrix[i][j] = (combinations_matrix[i - 1][j - 1] + combinations_matrix[i - 1][j]) % self.X
        return combinations_matrix
