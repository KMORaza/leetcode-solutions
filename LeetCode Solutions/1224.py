class Solution:
    def maxEqualFreq(self, nums):
        from collections import Counter
        freq = Counter()
        freq_count = Counter()
        max_len = 0
        for i, num in enumerate(nums):
            if freq[num]:
                freq_count[freq[num]] -= 1
                if freq_count[freq[num]] == 0:
                    del freq_count[freq[num]]
            freq[num] += 1
            freq_count[freq[num]] += 1
            if len(freq_count) == 1:
                key, count = next(iter(freq_count.items()))
                if key == 1 or count == 1:
                    max_len = i + 1
            elif len(freq_count) == 2:
                keys = list(freq_count.keys())
                values = list(freq_count.values())
                k1, k2 = keys[0], keys[1]
                v1, v2 = values[0], values[1]
                if (k1 == 1 and v1 == 1) or (k2 == 1 and v2 == 1):
                    max_len = i + 1
                elif (abs(k1 - k2) == 1 and ((k1 > k2 and v1 == 1) or (k2 > k1 and v2 == 1))):
                    max_len = i + 1
        return max_len
