class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(s: str, word: str) -> bool:
            it = iter(s)
            return all(char in it for char in word)
        dictionary.sort(key=lambda word: (-len(word), word))
        for word in dictionary:
            if is_subsequence(s, word):
                return word
        return ""
