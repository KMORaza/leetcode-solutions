class Solution:
    def stoneGameIX(self, game_stones):
        stone_count = [0, 0, 0]
        for single_stone in game_stones:
            stone_count[single_stone % 3] += 1
        if stone_count[0] % 2 == 0:
            return min(stone_count[1], stone_count[2]) > 0
        return (stone_count[1] - stone_count[2] > 2) or (stone_count[2] - stone_count[1] > 2)
