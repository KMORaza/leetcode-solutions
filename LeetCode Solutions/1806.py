class Solution:
    def reinitializePermutation(self, n: int) -> int:
        permutation = list(range(n))
        original = permutation[:]
        steps = 0
        while True:
            new_permutation = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    new_permutation[i] = permutation[i // 2]
                else:
                    new_permutation[i] = permutation[n // 2 + (i - 1) // 2]
            permutation = new_permutation
            steps += 1
            if permutation == original:
                break
        return steps
