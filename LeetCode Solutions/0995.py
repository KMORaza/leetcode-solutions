class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        flips = 0
        flip_effect = [0] * n
        current_flips = 0
        num_flips = 0
        for i in range(n):
            if i >= K:
                current_flips -= flip_effect[i - K]
            if (A[i] + current_flips) % 2 == 0:
                if i + K > n:
                    return -1
                current_flips += 1
                flip_effect[i] += 1
                num_flips += 1
        return num_flips
