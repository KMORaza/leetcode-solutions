class Solution:
    def uniqueLetterString(self, s: str) -> int:
        from collections import defaultdict
        index_list = defaultdict(lambda: [-1])
        for i, char in enumerate(s):
            index_list[char].append(i)
        for char in index_list:
            index_list[char].append(len(s))
        output = 0
        for occurences in index_list.values():
            for i in range(1, len(occurences) - 1):
                output += (occurences[i] - occurences[i - 1]) * (occurences[i + 1] - occurences[i])
        return output
