from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laser_counts = [row.count('1') for row in bank if '1' in row]
        total_beams = 0
        for i in range(len(laser_counts) - 1):
            total_beams += laser_counts[i] * laser_counts[i + 1]
        return total_beams
