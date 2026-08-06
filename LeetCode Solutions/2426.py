class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        import bisect

        n = len(nums1)
        d = [nums1[i] - nums2[i] for i in range(n)]

        result = 0
        sorted_list = []

        for i in range(n):
            target = d[i] + diff
            pos = bisect.bisect_right(sorted_list, target)
            result += pos

            insert_pos = bisect.bisect_left(sorted_list, d[i])
            sorted_list.insert(insert_pos, d[i])

        return result