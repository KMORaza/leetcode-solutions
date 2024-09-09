class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(word):
            groups = []
            n = len(word)
            i = 0
            while i < n:
                j = i
                while j < n and word[j] == word[i]:
                    j += 1
                groups.append((word[i], j - i))
                i = j
            return groups
        def is_stretchy(word_groups, s_groups):
            if len(word_groups) != len(s_groups):
                return False
            for (wc, w_len), (sc, s_len) in zip(word_groups, s_groups):
                if wc != sc or w_len > s_len or (s_len < 3 and w_len != s_len):
                    return False
            return True
        s_groups = get_groups(s)
        count = 0
        for word in words:
            word_groups = get_groups(word)
            if is_stretchy(word_groups, s_groups):
                count += 1
        return count
