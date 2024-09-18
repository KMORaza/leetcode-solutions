class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefixXOR = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            prefixXOR[i] = prefixXOR[i - 1] ^ arr[i - 1]
        count = 0
        xor_count = {}
        for j in range(1, len(arr) + 1):
            for i in range(j):
                if prefixXOR[j] == prefixXOR[i]:
                    count += (j - i - 1)
        return count
