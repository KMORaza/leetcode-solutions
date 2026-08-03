class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        curr_char = 'a'

        for c in key:
            if c != ' ' and c not in mapping:
                mapping[c] = curr_char
                curr_char = chr(ord(curr_char) + 1)

        result = []
        for c in message:
            if c == ' ':
                result.append(' ')
            else:
                result.append(mapping[c])

        return ''.join(result)