class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        negative = (numerator < 0) != (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            return f"{'-' if negative else ''}{integer_part}"
        decimal_part = []
        remainder_map = {}
        index = 0
        while remainder != 0:
            if remainder in remainder_map:
                start = remainder_map[remainder]
                decimal_part.insert(start, '(')
                decimal_part.append(')')
                break
            remainder_map[remainder] = index
            remainder *= 10
            decimal_part.append(str(remainder // denominator))
            remainder %= denominator
            index += 1
        return f"{'-' if negative else ''}{integer_part}." + ''.join(decimal_part)
