class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        import heapq
        from collections import Counter

        diffs = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        total_ops = k1 + k2

        if total_ops == 0:
            return sum(diff * diff for diff in diffs)

        count = Counter(diffs)
        heap = [(-diff, freq) for diff, freq in count.items()]
        heapq.heapify(heap)

        while total_ops > 0 and heap:
            max_diff, freq = heapq.heappop(heap)
            max_diff = -max_diff

            if not heap:
                ops_needed = max_diff * freq
                if ops_needed <= total_ops:
                    total_ops -= ops_needed
                    continue
                else:
                    reduce_by = total_ops // freq
                    remaining_ops = total_ops % freq
                    new_diff = max_diff - reduce_by
                    heapq.heappush(heap, (-(new_diff - 1), remaining_ops))
                    heapq.heappush(heap, (-(new_diff), freq - remaining_ops))
                    total_ops = 0
            else:
                next_max_diff = -heap[0][0]
                ops_needed = (max_diff - next_max_diff) * freq

                if ops_needed <= total_ops:
                    total_ops -= ops_needed
                    if next_max_diff > 0:
                        if heap and -heap[0][0] == next_max_diff:
                            old_freq = heapq.heappop(heap)[1]
                            heapq.heappush(heap, (-(next_max_diff), old_freq + freq))
                        else:
                            heapq.heappush(heap, (-(next_max_diff), freq))
                else:
                    reduce_by = total_ops // freq
                    remaining_ops = total_ops % freq
                    new_diff = max_diff - reduce_by
                    heapq.heappush(heap, (-(new_diff - 1), remaining_ops))
                    heapq.heappush(heap, (-(new_diff), freq - remaining_ops))
                    total_ops = 0

        result = 0
        while heap:
            diff, freq = heapq.heappop(heap)
            diff = -diff
            result += diff * diff * freq

        return result