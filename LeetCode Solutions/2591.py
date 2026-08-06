class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        money -= children
        eights = money // 7
        remainder = money % 7

        if eights > children:
            return children - 1

        if eights == children and remainder == 0:
            return children

        if eights == children - 1 and remainder == 3:
            return children - 2

        return min(eights, children - 1)