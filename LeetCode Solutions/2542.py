class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        from heapq import heappush, heappop

        pairs = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        pairs.sort(key=lambda x: x[1], reverse=True)

        min_heap = []
        sum_nums1 = 0
        max_score = 0

        for num1, num2 in pairs:
            heappush(min_heap, num1)
            sum_nums1 += num1

            if len(min_heap) > k:
                removed = heappop(min_heap)
                sum_nums1 -= removed

            if len(min_heap) == k:
                score = sum_nums1 * num2
                max_score = max(max_score, score)

        return max_score