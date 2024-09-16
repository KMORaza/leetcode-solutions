class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        num_bits = n.bit_length()
        bitmask = (1 << num_bits) - 1
        return bitmask ^ n
