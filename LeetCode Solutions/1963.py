class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_balance = 0
        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
            max_balance = max(max_balance, -balance)
        return (max_balance + 1) // 2
