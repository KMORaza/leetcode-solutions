class Solution:
    def fillCups(self, amount):
        amount.sort(reverse=True)
        a, b, c = amount[0], amount[1], amount[2]

        if a >= b + c:
            return a
        else:
            total = a + b + c
            return (total + 1) // 2