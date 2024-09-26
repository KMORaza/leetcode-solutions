class Solution:
    def numberOfUniqueGoodSubsequences(self, binary_string: str) -> int:
        x = 1000000007
        subseq_count = [0, 0]
        for symbol in binary_string:
            subseq_count[int(symbol)] = (subseq_count[0] + subseq_count[1]) % x
            if symbol == '1':
                subseq_count[1] += 1
        return (subseq_count[0] + subseq_count[1] + (1 if '0' in binary_string else 0)) % x
