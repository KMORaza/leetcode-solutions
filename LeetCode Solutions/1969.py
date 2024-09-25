class Solution:
    x = 1000000007
    def minNonZeroProduct(self, exponent: int) -> int:
        totalItems = 1 << exponent
        countHalf = totalItems // 2 - 1
        return int((self.power_modulation(totalItems - 2, countHalf) * ((totalItems - 1) % self.x)) % self.x)
    def power_modulation(self, baseValue: int, expValue: int) -> int:
        if expValue == 0:
            return 1
        baseValue %= self.x
        if expValue % 2 == 1:
            return (baseValue * self.power_modulation(baseValue, expValue - 1)) % self.x
        return self.power_modulation(baseValue * baseValue, expValue // 2) % self.x