class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        first_index = {}
        last_index = {}
        for i, color in enumerate(colors):
            if color not in first_index:
                first_index[color] = i
            last_index[color] = i
        max_distance = 0
        for color in first_index:
            for other_color in last_index:
                if color != other_color:
                    distance = max(last_index[other_color] - first_index[color], first_index[other_color] - last_index[color])
                    max_distance = max(max_distance, distance)
        return max_distance
