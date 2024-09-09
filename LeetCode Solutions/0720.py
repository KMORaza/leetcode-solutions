class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        built_words = set([""])
        longest_word = ""
        for word in words:
            if word[:-1] in built_words:
                built_words.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word
