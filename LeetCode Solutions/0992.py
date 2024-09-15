class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atMostK(K: int) -> int:
            count = 0
            left = 0
            freq = collections.defaultdict(int)
            for right in range(len(A)):
                if freq[A[right]] == 0:
                    K -= 1
                freq[A[right]] += 1
                while K < 0:
                    freq[A[left]] -= 1
                    if freq[A[left]] == 0:
                        K += 1
                    left += 1
                count += right - left + 1
            return count
        return atMostK(K) - atMostK(K - 1)
