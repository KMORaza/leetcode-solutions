class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        power = [0] * n

        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            power[left] += stations[i]
            if right + 1 < n:
                power[right + 1] -= stations[i]

        for i in range(1, n):
            power[i] += power[i - 1]

        def can_achieve(min_power):
            added = [0] * n
            total_added = 0
            current_add = 0

            for i in range(n):
                current_add += added[i]
                current_power = power[i] + current_add

                if current_power < min_power:
                    needed = min_power - current_power
                    total_added += needed
                    if total_added > k:
                        return False

                    current_add += needed
                    right = min(n - 1, i + 2 * r)
                    if right + 1 < n:
                        added[right + 1] -= needed

            return True

        left, right = 0, sum(stations) + k
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_achieve(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result