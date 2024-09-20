class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i
        encoded_xor = 0
        for i in range(1, len(encoded), 2):
            encoded_xor ^= encoded[i]
        first = total ^ encoded_xor
        result = [first]
        for num in encoded:
            first ^= num
            result.append(first)
        return result
