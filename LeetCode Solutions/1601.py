from typing import List
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def is_valid(building_delta: List[int]) -> bool:
            return all(delta == 0 for delta in building_delta)
        max_requests = 0
        total_requests = len(requests)
        for mask in range(1 << total_requests):
            building_delta = [0] * n
            current_request_count = 0
            for i in range(total_requests):
                if mask & (1 << i):
                    from_building, to_building = requests[i]
                    building_delta[from_building] -= 1
                    building_delta[to_building] += 1
                    current_request_count += 1
            if is_valid(building_delta):
                max_requests = max(max_requests, current_request_count)
        return max_requests
