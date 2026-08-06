class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        indexed_heights = [(heights[i], i) for i in range(len(heights))]
        indexed_heights.sort(reverse=True)

        result = []
        for height, idx in indexed_heights:
            result.append(names[idx])

        return result