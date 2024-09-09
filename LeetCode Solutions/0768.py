class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_seen = float('-inf')
        for i in range(len(arr)):
            max_seen = max(max_seen, arr[i])
            min_remaining = min(arr[i+1:], default=float('inf'))
            if max_seen <= min_remaining:
                chunks += 1
        return chunks
