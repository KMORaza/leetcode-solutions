class Solution:
    def minimumTotalCost(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        conflicts = []
        freq = {}

        for i in range(n):
            if nums1[i] == nums2[i]:
                conflicts.append(i)
                v = nums1[i]
                freq[v] = freq.get(v, 0) + 1

        if not conflicts:
            return 0

        max_val = max(freq, key=freq.get)
        max_cnt = freq[max_val]
        k = len(conflicts)

        need_external = max(0, 2 * max_cnt - k)

        valid_non_conflicts = []
        for i in range(n):
            if nums1[i] != nums2[i] and nums1[i] != max_val and nums2[i] != max_val:
                valid_non_conflicts.append(i)

        if len(valid_non_conflicts) < need_external:
            return -1

        valid_non_conflicts.sort()
        external_cost = sum(valid_non_conflicts[:need_external])
        conflict_cost = sum(conflicts)

        return conflict_cost + external_cost