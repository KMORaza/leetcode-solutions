class Solution:
    def maxNumberOfFamilies(self, totalRows: int, occupiedSeats: list[list[int]]) -> int:
        totalGroups = 0
        row_to_bitmask = {}
        for seat in occupiedSeats:
            rowIndex, seatNumber = seat
            if rowIndex not in row_to_bitmask:
                row_to_bitmask[rowIndex] = 0
            row_to_bitmask[rowIndex] |= 1 << (seatNumber - 1)
        for bitmask in row_to_bitmask.values():
            if (bitmask & 0b0111111110) == 0:
                totalGroups += 2
            elif (bitmask & 0b0111100000) == 0 or (bitmask & 0b0001111000) == 0 or (bitmask & 0b0000011110) == 0:
                totalGroups += 1
        return totalGroups + (totalRows - len(row_to_bitmask)) * 2
