class Fancy:
    x = 1000000007
    def __init__(self):
        self.values = []
        self.multiplier = 1
        self.offset = 0
    def append(self, input_value):
        transformed_value = (input_value - self.offset + self.x) % self.x
        self.values.append(transformed_value * self.moduloFunction(self.multiplier, self.x - 2) % self.x)
    def addAll(self, increment):
        self.offset = (self.offset + increment) % self.x
    def multAll(self, multiplier):
        self.multiplier = (self.multiplier * multiplier) % self.x
        self.offset = (self.offset * multiplier) % self.x
    def getIndex(self, index):
        if index >= len(self.values):
            return -1
        return (self.multiplier * self.values[index] + self.offset) % self.x
    def moduloFunction(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent % 2 == 1:
            return (base * self.moduloFunction(base % self.x, exponent - 1)) % self.x
        half_pow = self.moduloFunction(base * base % self.x, exponent // 2)
        return half_pow % self.x
