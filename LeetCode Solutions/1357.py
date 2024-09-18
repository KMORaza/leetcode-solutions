class Cashier:
    def __init__(self, interval: int, discount_rate: int, item_ids: list[int], item_prices: list[int]):
        self.interval = interval
        self.discount_rate = discount_rate
        self.item_to_price = dict(zip(item_ids, item_prices))
        self.transaction_count = 0
    def getBill(self, items: list[int], quantities: list[int]) -> float:
        self.transaction_count += 1
        total_amount = sum(self.item_to_price[item] * qty for item, qty in zip(items, quantities))
        if self.transaction_count % self.interval == 0:
            return total_amount * (1 - self.discount_rate / 100.0)
        return total_amount
