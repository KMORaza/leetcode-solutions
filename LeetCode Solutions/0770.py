from collections import defaultdict
import re
class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: list[str], evalints: list[int]) -> list[str]:
        var_to_idx = {var: idx for idx, var in enumerate(evalvars)}
        return self.parse(expression, var_to_idx, evalints)
    def parse(self, expr: str, var_to_idx: dict, evalints: list[int]) -> list[str]:
        n = len(expr)
        i = 0
        output = []
        while i < n:
            if expr[i] == '(':
                cnt = 1
                j = i + 1
                while j < n and cnt:
                    if expr[j] == '(':
                        cnt += 1
                    elif expr[j] == ')':
                        cnt -= 1
                    j += 1
                cur = self.parse(expr[i + 1:j - 1], var_to_idx, evalints)
                output.extend(cur)
                i = j
            elif expr[i].isalpha():
                j = i + 1
                while j < n and (expr[j].isalnum() or expr[j] == '_'):
                    j += 1
                var = expr[i:j]
                if var in var_to_idx:
                    output.append(f"{evalints[var_to_idx[var]]}*{var}")
                else:
                    output.append(f"1*{var}")
                i = j
            else:
                j = i + 1
                while j < n and expr[j].isdigit():
                    j += 1
                if j > i:
                    output.append(expr[i:j])
                i = j
        return self.simplify(output)
    def simplify(self, terms: list[str]) -> list[str]:
        count = defaultdict(int)
        for term in terms:
            if not term:
                continue
            sign = 1
            i = 0
            if term[0] == '-':
                sign = -1
                i += 1
            elif term[0] == '+':
                i += 1
            while i < len(term) and term[i] != '*':
                i += 1
            if i == 0:
                num = sign
            else:
                num_part = term[:i].strip()
                try:
                    num = int(num_part) * sign
                except ValueError:
                    num = sign
            var = term[i + 1:].strip()
            count[var] += num
        res = [(var, coef) for var, coef in count.items() if coef != 0]
        res.sort(key=lambda x: (-len(x[0]), x[0]))
        output = []
        for var, coef in res:
            if coef == 1:
                output.append(f"{var}")
            elif coef == -1:
                output.append(f"-{var}")
            else:
                output.append(f"{coef}*{var}")
        return output
