class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        prefix = ''
        for word in words:
            prefix += word
            if prefix == s:
                return True
            if len(prefix) > len(s):
                break
        return False
