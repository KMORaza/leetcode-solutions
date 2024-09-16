from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for start, end, seats in bookings:
            diff[start - 1] += seats
            if end < n:
                diff[end] -= seats
        result = [0] * n
        current_seats = 0
        for i in range(n):
            current_seats += diff[i]
            result[i] = current_seats
        return result
