class Solution:
    def __init__(self):
        self.array = [0] * 12
        self.memoization = [[-1] * 2 for _ in range(12)]
        self.set = set()
    def atMostNGivenDigitSet(self, digits, n):
        self.memoization = [[-1] * 2 for _ in range(12)]
        self.set = set(int(digit) for digit in digits)
        length = 0
        temp_n = n
        while temp_n > 0:
            length += 1
            self.array[length] = temp_n % 10
            temp_n //= 10
        return self.dfs(length, 1, True)
    def dfs(self, position, leader, limit):
        if position <= 0:
            return 1 if leader == 0 else 0
        if not limit and leader != 1 and self.memoization[position][leader] != -1:
            return self.memoization[position][leader]
        count = 0
        upper_bound = self.array[position] if limit else 9
        for i in range(upper_bound + 1):
            if i == 0 and leader == 1:
                count += self.dfs(position - 1, leader, limit and i == upper_bound)
            elif i in self.set:
                count += self.dfs(position - 1, 0, limit and i == upper_bound)
        if not limit and leader == 0:
            self.memoization[position][leader] = count
        return count
