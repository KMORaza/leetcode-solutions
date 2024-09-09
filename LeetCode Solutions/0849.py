class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_distance = 0
        last_person = -1
        for i in range(n):
            if seats[i] == 1:
                if last_person == -1:
                    max_distance = i
                else:
                    max_distance = max(max_distance, (i - last_person) // 2)
                last_person = i
        if last_person != n - 1:
            max_distance = max(max_distance, n - 1 - last_person)
        return max_distance
