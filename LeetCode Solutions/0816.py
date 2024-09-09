class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        length = len(s)
        results = []
        for i in range(2, length - 1):
            for x in self.getPossibleNumbers(s, 1, i):
                for y in self.getPossibleNumbers(s, i, length - 1):
                    results.append(f"({x}, {y})")
        return results
    def getPossibleNumbers(self, s: str, start: int, end: int) -> list[str]:
        possible_nums = []
        for k in range(1, end - start + 1):
            left_part = s[start:start + k]
            right_part = s[start + k:end]
            is_valid = (left_part == "0" or not left_part.startswith("0")) and not right_part.endswith("0")
            if is_valid:
                possible_nums.append(left_part + ('.' + right_part if k < end - start else ''))
        return possible_nums
