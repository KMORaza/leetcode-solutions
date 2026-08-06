class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = len(s)
        first_occurrence = {}

        for i in range(n):
            char = s[i]
            if char in first_occurrence:
                first_idx = first_occurrence[char]
                actual_distance = i - first_idx - 1
                expected_distance = distance[ord(char) - ord('a')]
                if actual_distance != expected_distance:
                    return False
            else:
                first_occurrence[char] = i

        return True