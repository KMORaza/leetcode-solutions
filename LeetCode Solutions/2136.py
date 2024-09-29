from typing import List
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        flowers = sorted(zip(plantTime, growTime), key=lambda x: -x[1])
        total_time = 0
        max_bloom_time = 0
        for plant, grow in flowers:
            total_time += plant
            max_bloom_time = max(max_bloom_time, total_time + grow)
        return max_bloom_time
