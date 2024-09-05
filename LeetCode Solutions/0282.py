class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        def backtrack(index: int, prev_num: int, current_val: int, expr: str):
            if index == len(num):
                if current_val == target:
                    results.append(expr)
                return
            for i in range(index + 1, len(num) + 1):
                current_str = num[index:i]
                if len(current_str) > 1 and current_str[0] == '0':
                    continue
                current_num = int(current_str)
                if index == 0:
                    backtrack(i, current_num, current_num, current_str)
                else:
                    backtrack(i, current_num, current_val + current_num, expr + '+' + current_str)
                    backtrack(i, -current_num, current_val - current_num, expr + '-' + current_str)
                    backtrack(i, prev_num * current_num, (current_val - prev_num) + (prev_num * current_num), expr + '*' + current_str)
        results = []
        backtrack(0, 0, 0, '')
        return results