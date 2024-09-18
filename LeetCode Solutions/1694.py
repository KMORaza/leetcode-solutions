class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = [ch for ch in number if ch.isdigit()]
        result = []
        while len(digits) > 0:
            if len(digits) > 4:
                result.append(''.join(digits[:3]))
                digits = digits[3:]
            elif len(digits) == 4:
                result.append(''.join(digits[:2]))
                result.append(''.join(digits[2:]))
                break
            else:
                result.append(''.join(digits))
                break
        return '-'.join(result)
