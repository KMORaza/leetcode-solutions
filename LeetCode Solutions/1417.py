class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)
        if abs(len(letters) - len(digits)) > 1:
            return ""
        result = []
        if len(letters) > len(digits):
            result = self._interleave(letters, digits)
        else:
            result = self._interleave(digits, letters)
        return ''.join(result)
    def _interleave(self, longer_list, shorter_list):
        result = []
        i = 0
        j = 0
        while i < len(longer_list) or j < len(shorter_list):
            if i < len(longer_list):
                result.append(longer_list[i])
                i += 1
            if j < len(shorter_list):
                result.append(shorter_list[j])
                j += 1
        return result
