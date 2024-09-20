class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(s):
            s = list(s)
            n = len(s)
            i = n - 2
            while i >= 0 and s[i] >= s[i + 1]:
                i -= 1
            if i == -1:
                return False
            j = n - 1
            while s[j] <= s[i]:
                j -= 1
            s[i], s[j] = s[j], s[i]
            s[i + 1:] = reversed(s[i + 1:])
            return ''.join(s)
        target = num
        for _ in range(k):
            target = next_permutation(target)
        swaps = 0
        num_list = list(num)
        for i in range(len(num)):
            if num_list[i] != target[i]:
                j = i + 1
                while num_list[j] != target[i]:
                    j += 1
                while j > i:
                    num_list[j], num_list[j - 1] = num_list[j - 1], num_list[j]
                    swaps += 1
                    j -= 1
        return swaps
