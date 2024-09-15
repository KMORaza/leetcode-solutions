from typing import List
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        if x == 1 and y == 1:
            if bound >= 2:
                return [2]
            else:
                return []
        if x == 1:
            y_powers = []
            power = 1
            while power <= bound:
                y_powers.append(power)
                power *= y
            for y_power in y_powers:
                if y_power + 1 <= bound:
                    result.add(y_power + 1)
            return sorted(result)
        if y == 1:
            x_powers = []
            power = 1
            while power <= bound:
                x_powers.append(power)
                power *= x
            for x_power in x_powers:
                if x_power + 1 <= bound:
                    result.add(x_power + 1)
            return sorted(result)
        x_powers = []
        y_powers = []
        power = 1
        while power <= bound:
            x_powers.append(power)
            power *= x
        power = 1
        while power <= bound:
            y_powers.append(power)
            power *= y
        for x_power in x_powers:
            for y_power in y_powers:
                if x_power + y_power <= bound:
                    result.add(x_power + y_power)
        return sorted(result)
