class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        while word1 and word2:
            if word1 > word2:
                merge.append(word1[0])
                word1 = word1[1:]
            else:
                merge.append(word2[0])
                word2 = word2[1:]
        merge.append(word1)
        merge.append(word2)
        return ''.join(merge)
