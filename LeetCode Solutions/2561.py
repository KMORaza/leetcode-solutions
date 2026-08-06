class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        from collections import Counter

        c1 = Counter(basket1)
        c2 = Counter(basket2)

        all_keys = set(c1.keys()) | set(c2.keys())
        global_min = float('inf')

        excess1 = []
        excess2 = []

        for k in all_keys:
            total = c1.get(k, 0) + c2.get(k, 0)
            if total % 2 != 0:
                return -1
            diff = c1.get(k, 0) - c2.get(k, 0)
            if diff > 0:
                excess1.extend([k] * (diff // 2))
            elif diff < 0:
                excess2.extend([k] * ((-diff) // 2))
            global_min = min(global_min, k)

        if len(excess1) != len(excess2):
            return -1

        excess1.sort()
        excess2.sort(reverse=True)

        cost = 0
        for a, b in zip(excess1, excess2):
            direct = min(a, b)
            via_min = 2 * global_min
            cost += min(direct, via_min)

        return cost