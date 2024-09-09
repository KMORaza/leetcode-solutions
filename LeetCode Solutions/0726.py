from collections import defaultdict, deque
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(formula: str) -> dict:
            stack = deque([defaultdict(int)])
            i = 0
            n = len(formula)
            def get_elem():
                nonlocal i
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                return formula[start:i]
            def get_num():
                nonlocal i
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                return int(formula[start:i]) if start != i else 1
            while i < n:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    i += 1
                    num = get_num()
                    top = stack.pop()
                    for elem, count in top.items():
                        stack[-1][elem] += count * num
                else:
                    elem = get_elem()
                    num = get_num()
                    stack[-1][elem] += num
            return stack.pop()
        count = parse(formula)
        ans = []
        for elem in sorted(count):
            freq = count[elem]
            ans.append(elem)
            if freq > 1:
                ans.append(str(freq))
        return ''.join(ans)
