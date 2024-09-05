import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        seen = set()
        seen.add(1)
        ugly_number = 1
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            for prime in primes:
                new_ugly = ugly_number * prime
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return ugly_number

