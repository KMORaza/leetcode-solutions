class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        memo = {}
        def can_win(available: int, current_total: int) -> bool:
            if current_total >= desiredTotal:
                return False
            if available in memo:
                return memo[available]
            for i in range(maxChoosableInteger):
                if available & (1 << i):
                    new_total = current_total + (i + 1)
                    new_available = available & ~(1 << i)
                    if not can_win(new_available, new_total):
                        memo[available] = True
                        return True
            memo[available] = False
            return False
        initial_available = (1 << maxChoosableInteger) - 1
        return can_win(initial_available, 0)
