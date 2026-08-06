class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return -1

        def get_prime_factors(num):
            factors = set()
            d = 2
            while d * d <= num:
                while num % d == 0:
                    factors.add(d)
                    num //= d
                d += 1
            if num > 1:
                factors.add(num)
            return factors

        prime_sets = []
        for num in nums:
            prime_sets.append(get_prime_factors(num))

        last_occurrence = {}
        for i in range(n):
            for prime in prime_sets[i]:
                last_occurrence[prime] = i

        first_occurrence = {}
        for i in range(n):
            for prime in prime_sets[i]:
                if prime not in first_occurrence:
                    first_occurrence[prime] = i

        intervals = []
        for prime in last_occurrence:
            if first_occurrence[prime] != last_occurrence[prime]:
                intervals.append((first_occurrence[prime], last_occurrence[prime]))

        if not intervals:
            return 0

        intervals.sort()

        max_end = 0

        for start, end in intervals:
            if start > max_end:
                return max_end
            max_end = max(max_end, end)

        return -1 if max_end == n - 1 else max_end