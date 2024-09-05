class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            num_papers_with_at_least_mid_citations = n - mid
            if citations[mid] >= num_papers_with_at_least_mid_citations:
                right = mid - 1
            else:
                left = mid + 1
        return n - left