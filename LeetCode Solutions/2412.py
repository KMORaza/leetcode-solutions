class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_loss = 0
        max_cash_back = 0
        max_need = 0

        for cost, cashback in transactions:
            if cost > cashback:
                total_loss += cost - cashback
                max_cash_back = max(max_cash_back, cashback)
            else:
                max_need = max(max_need, cost)

        return total_loss + max(max_cash_back, max_need)