class Solution:
    def oddString(self, words: List[str]) -> str:
        def get_diff_arr(word):
            diff = []
            for i in range(1, len(word)):
                diff.append(ord(word[i]) - ord(word[i - 1]))
            return tuple(diff)

        diff_map = {}
        for word in words:
            diff_tuple = get_diff_arr(word)
            if diff_tuple not in diff_map:
                diff_map[diff_tuple] = []
            diff_map[diff_tuple].append(word)

        for diff_tuple, word_list in diff_map.items():
            if len(word_list) == 1:
                return word_list[0]