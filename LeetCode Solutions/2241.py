from typing import List
class ATM:
    def __init__(self):
        self.bills = [0] * 5
        self.denominations = [20, 50, 100, 200, 500]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.bills[i] += banknotesCount[i]
    def withdraw(self, amount: int) -> List[int]:
        if amount % 10 != 0:
            return [-1]
        withdrawal = [0] * 5
        remaining_amount = amount
        for i in range(4, -1, -1):
            if remaining_amount <= 0:
                break
            needed_bills = remaining_amount // self.denominations[i]
            available_bills = self.bills[i]
            count = min(needed_bills, available_bills)
            withdrawal[i] = count
            remaining_amount -= count * self.denominations[i]
            self.bills[i] -= count
        if remaining_amount > 0:
            for i in range(5):
                self.bills[i] += withdrawal[i]
            return [-1]
        return withdrawal