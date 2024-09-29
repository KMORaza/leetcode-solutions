from sortedcontainers import SortedList
class StockPrice:
    def __init__(self):
        self.timestamp_to_price = {}
        self.sorted_prices = SortedList()
        self.current_timestamp = 0
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timestamp_to_price:
            old_price = self.timestamp_to_price[timestamp]
            self.sorted_prices.remove(old_price)
        else:
            self.current_timestamp = max(self.current_timestamp, timestamp)
        self.timestamp_to_price[timestamp] = price
        self.sorted_prices.add(price)
    def current(self) -> int:
        return self.timestamp_to_price[self.current_timestamp]
    def maximum(self) -> int:
        return self.sorted_prices[-1]
    def minimum(self) -> int:
        return self.sorted_prices[0]