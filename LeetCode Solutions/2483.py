class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        min_penalty = float('inf')
        best_hour = 0
        current_penalty = customers.count('Y')

        if current_penalty < min_penalty:
            min_penalty = current_penalty
            best_hour = 0

        for i in range(n):
            if customers[i] == 'Y':
                current_penalty -= 1
            else:
                current_penalty += 1

            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_hour = i + 1

        return best_hour