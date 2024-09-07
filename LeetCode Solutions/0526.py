class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(index: int) -> int:
            if index > n:
                return 1
            count = 0
            for num in range(1, n + 1):
                if not used[num]:
                    if num % index == 0 or index % num == 0:
                        used[num] = True
                        count += backtrack(index + 1)
                        used[num] = False
            return count
        used = [False] * (n + 1)
        return backtrack(1)
