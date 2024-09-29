from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for seat, student in zip(seats, students):
            moves += (seat - student) if seat >= student else (student - seat)
        return moves
