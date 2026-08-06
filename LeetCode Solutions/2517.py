class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)

        def can_achieve_tastiness(target):
            count = 1
            last_selected = price[0]

            for i in range(1, n):
                if price[i] - last_selected >= target:
                    count += 1
                    last_selected = price[i]
                    if count == k:
                        return True

            return False

        left, right = 0, price[-1] - price[0]
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_achieve_tastiness(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result