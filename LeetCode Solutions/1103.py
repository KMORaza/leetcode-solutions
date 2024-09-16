from typing import List
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        current_candy = 1
        while candies > 0:
            for i in range(num_people):
                if candies >= current_candy:
                    result[i] += current_candy
                    candies -= current_candy
                else:
                    result[i] += candies
                    candies = 0
                current_candy += 1
                if candies == 0:
                    break
        return result
