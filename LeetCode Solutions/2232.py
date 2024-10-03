class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_position = expression.index('+')
        lhs = expression[:plus_position]
        rhs = expression[plus_position + 1:]
        best_expression = ""
        minimum_value = float('inf')
        for left_cut in range(len(lhs)):
            for right_cut in range(len(rhs)):
                x = int(lhs[:left_cut]) if left_cut > 0 else 1
                y = int(lhs[left_cut:])
                z = int(rhs[:right_cut + 1])
                w = int(rhs[right_cut + 1:]) if right_cut < len(rhs) - 1 else 1
                current_result = x * (y + z) * w
                if current_result < minimum_value:
                    minimum_value = current_result
                    best_expression = ("" if left_cut == 0 else str(x)) + '(' + str(y) + '+' + str(z) + ')' + ("" if right_cut == len(rhs) - 1 else str(w))
        return best_expression
