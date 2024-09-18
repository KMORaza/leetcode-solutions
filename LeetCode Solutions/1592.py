class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space_count = text.count(' ')
        if len(words) == 1:
            return words[0] + ' ' * space_count
        gaps = len(words) - 1
        spaces_between = space_count // gaps
        extra_spaces = space_count % gaps
        result = (' ' * spaces_between).join(words)
        result += ' ' * extra_spaces
        return result
