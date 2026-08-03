class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for k, trim in queries:
            trimmed_with_index = []
            for i, num_str in enumerate(nums):
                trimmed = num_str[-trim:]
                trimmed_with_index.append((trimmed, i))

            trimmed_with_index.sort(key=lambda x: (x[0], x[1]))
            result.append(trimmed_with_index[k - 1][1])

        return result