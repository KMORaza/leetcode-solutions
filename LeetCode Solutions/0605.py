class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if prev_empty and next_empty:
                    count += 1
                    flowerbed[i] = 1
            i += 1
        return count >= n
