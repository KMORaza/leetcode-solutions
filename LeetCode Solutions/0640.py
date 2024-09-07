class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse_side(side: str) -> (int, int):
            coeff_x = 0
            const_sum = 0
            i = 0
            n = len(side)
            while i < n:
                if side[i] in '+-':
                    sign = 1 if side[i] == '+' else -1
                    i += 1
                    if i < n and side[i].isdigit():
                        j = i
                        while j < n and side[j].isdigit():
                            j += 1
                        num = int(side[i:j])
                        i = j
                        if i < n and side[i] == 'x':
                            coeff_x += sign * num
                            i += 1
                        else:
                            const_sum += sign * num
                    elif i < n and side[i] == 'x':
                        coeff_x += sign
                        i += 1
                else:
                    if side[i].isdigit():
                        j = i
                        while j < n and side[j].isdigit():
                            j += 1
                        num = int(side[i:j])
                        i = j
                        if i < n and side[i] == 'x':
                            coeff_x += num
                            i += 1
                        else:
                            const_sum += num
                    elif side[i] == 'x':
                        coeff_x += 1
                        i += 1
            return coeff_x, const_sum
        left, right = equation.split('=')
        left_coeff_x, left_const = parse_side(left)
        right_coeff_x, right_const = parse_side(right)
        total_coeff_x = left_coeff_x - right_coeff_x
        total_const = right_const - left_const
        if total_coeff_x == 0:
            if total_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x_value = total_const // total_coeff_x
            return f"x={x_value}"
