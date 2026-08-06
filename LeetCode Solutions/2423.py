class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter

        freq = Counter(word)
        count_of_freq = Counter(freq.values())

        unique_freqs = sorted(count_of_freq.keys())

        if len(unique_freqs) == 1:
            freq_val = unique_freqs[0]
            num_chars = len(freq)

            if freq_val == 1:
                return True
            elif num_chars == 1:
                return True
            elif num_chars * freq_val == len(word) and freq_val == 1:
                return True
            else:
                return num_chars == 1
        elif len(unique_freqs) == 2:
            f1, f2 = unique_freqs
            c1, c2 = count_of_freq[f1], count_of_freq[f2]

            if f1 == 1 and c1 == 1:
                return True
            if f2 == 1 and c2 == 1:
                return True
            if f1 == f2 - 1 and c2 == 1:
                return True
            if f2 == f1 - 1 and c1 == 1:
                return True
            return False
        else:
            return False