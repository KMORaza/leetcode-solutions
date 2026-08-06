class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def count_bits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count

        unique_nums = list(set(nums))
        bit_counts = [count_bits(x) for x in unique_nums]
        bit_counts.sort()

        n = len(bit_counts)
        result = 0

        for i in range(n):
            target = k - bit_counts[i]
            # Find the first index j where bit_counts[j] >= target
            left, right = 0, n - 1
            pos = n
            while left <= right:
                mid = (left + right) // 2
                if bit_counts[mid] >= target:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1

            result += n - pos

        return result