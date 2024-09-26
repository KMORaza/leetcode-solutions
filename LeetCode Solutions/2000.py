class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word
        prefix_reversed = word[:index + 1][::-1]
        return prefix_reversed + word[index + 1:]
