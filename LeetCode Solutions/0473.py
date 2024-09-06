class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        side_length = total_length // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side_length
            current_matchstick = matchsticks[index]
            for i in range(4):
                if sides[i] + current_matchstick <= side_length:
                    sides[i] += current_matchstick
                    if backtrack(index + 1):
                        return True
                    sides[i] -= current_matchstick
                if sides[i] == 0:
                    break
            return False
        return backtrack(0)
