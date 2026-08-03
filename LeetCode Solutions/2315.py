class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        inside_pair = False

        for c in s:
            if c == '|':
                inside_pair = not inside_pair
            elif c == '*':
                if not inside_pair:
                    count += 1

        return count