class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_seen = 0
        for i in range(len(arr)):
            max_seen = max(max_seen, arr[i])
            if max_seen == i:
                chunks += 1
        return chunks
