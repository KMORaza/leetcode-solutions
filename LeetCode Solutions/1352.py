class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]
        self.last_zero_index = -1
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]
            self.last_zero_index = len(self.prefix_products) - 1
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)
    def getProduct(self, k: int) -> int:
        if len(self.prefix_products) - 1 - self.last_zero_index < k:
            return 0
        return self.prefix_products[-1] // self.prefix_products[-1 - k]
