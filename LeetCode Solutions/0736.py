class Solution:
    def evaluate(self, expression: str) -> int:
        return self._evaluate(expression, {})
    def _evaluate(self, expr: str, scope: dict) -> int:
        if expr[0].isdigit() or (expr[0] == '-' and expr[1].isdigit()):
            return int(expr)
        if expr in scope:
            return scope[expr]
        next_expr = expr[1:-1]
        tokens = self._split(next_expr)
        if tokens[0] == 'add':
            return self._evaluate(tokens[1], scope) + self._evaluate(tokens[2], scope)
        elif tokens[0] == 'mult':
            return self._evaluate(tokens[1], scope) * self._evaluate(tokens[2], scope)
        elif tokens[0] == 'let':
            new_scope = dict(scope)
            i = 1
            while i < len(tokens) - 1:
                new_scope[tokens[i]] = self._evaluate(tokens[i + 1], new_scope)
                i += 2
            return self._evaluate(tokens[-1], new_scope)
        else:
            raise ValueError(f"Unknown operation: {tokens[0]}")
    def _split(self, expr: str) -> list:
        tokens = []
        s = ''
        opened = 0
        for c in expr:
            if c == '(':
                opened += 1
            elif c == ')':
                opened -= 1
            if opened == 0 and c == ' ':
                if s:
                    tokens.append(s)
                    s = ''
            else:
                s += c
        if s:
            tokens.append(s)
        return tokens
