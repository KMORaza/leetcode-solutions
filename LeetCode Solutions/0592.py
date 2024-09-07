from math import gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def parse_fractions(expression: str):
            fractions = []
            i = 0
            n = len(expression)
            while i < n:
                sign = 1
                if expression[i] == '+':
                    i += 1
                elif expression[i] == '-':
                    sign = -1
                    i += 1
                num_start = i
                while i < n and expression[i] != '/':
                    i += 1
                numerator = int(expression[num_start:i])
                i += 1
                denom_start = i
                while i < n and (expression[i] == '/' or expression[i].isdigit()):
                    i += 1
                denominator = int(expression[denom_start:i])
                fractions.append((sign * numerator, denominator))
            return fractions
        def add_fractions(fractions):
            num, denom = 0, 1
            for numerator, denominator in fractions:
                common_denom = denom * denominator
                num = num * denominator + numerator * denom
                denom = common_denom
                common_gcd = gcd(num, denom)
                num //= common_gcd
                denom //= common_gcd
            return (num, denom)
        fractions = self.parse_fractions(expression)
        numerator, denominator = self.add_fractions(fractions)
        return f"{numerator}/{denominator}"
    def parse_fractions(self, expression: str):
        fractions = []
        i = 0
        n = len(expression)
        while i < n:
            sign = 1
            if expression[i] == '+':
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1
            num_start = i
            while i < n and expression[i] != '/':
                i += 1
            numerator = int(expression[num_start:i])
            i += 1
            denom_start = i
            while i < n and (expression[i] == '/' or expression[i].isdigit()):
                i += 1
            denominator = int(expression[denom_start:i])
            fractions.append((sign * numerator, denominator))
        return fractions
    def add_fractions(self, fractions):
        num, denom = 0, 1
        for numerator, denominator in fractions:
            common_denom = denom * denominator
            num = num * denominator + numerator * denom
            denom = common_denom
            common_gcd = gcd(num, denom)
            num //= common_gcd
            denom //= common_gcd
        return (num, denom)
