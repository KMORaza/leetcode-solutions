class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = 0
        consecutive_lates = 0
        for char in s:
            if char == 'A':
                absences += 1
                if absences >= 2:
                    return False
            if char == 'L':
                consecutive_lates += 1
                if consecutive_lates >= 3:
                    return False
            else:
                consecutive_lates = 0
        return True
