class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def min_operations(x):
            if x == 0:
                return 0
            length = x.bit_length()
            return (1 << length) - 1 - min_operations(x ^ (1 << (length - 1)))
        return min_operations(n)
