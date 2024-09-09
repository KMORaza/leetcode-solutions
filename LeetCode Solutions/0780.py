class Solution:
    def reachingPoints(self, startX: int, startY: int, targetX: int, targetY: int) -> bool:
        while targetX > startX and targetY > startY and targetX != targetY:
            if targetX > targetY:
                targetX %= targetY
            else:
                targetY %= targetX
        if targetX == startX and targetY == startY:
            return True
        if targetX == startX:
            return targetY > startY and (targetY - startY) % startX == 0
        if targetY == startY:
            return targetX > startX and (targetX - startX) % targetY == 0
        return False
