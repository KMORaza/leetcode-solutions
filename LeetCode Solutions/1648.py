class Solution:
    x = 1000000007
    def maxProfit(self, inventory, orders):
        inventory.sort()
        n = len(inventory)
        inventory.reverse()
        total_profit = 0
        current_index = 0
        while orders > 0:
            while current_index < n and inventory[current_index] >= inventory[0]:
                current_index += 1
            next_highest_value = inventory[current_index] if current_index < n else 0
            item_count = current_index
            price_difference = inventory[0] - next_highest_value
            potential_orders = item_count * price_difference
            if potential_orders > orders:
                decrement_value = orders // item_count
                first_term = inventory[0] - decrement_value + 1
                last_term = inventory[0]
                total_profit += (first_term + last_term) * decrement_value // 2 * item_count
                total_profit += (first_term - 1) * (orders % item_count)
            else:
                first_term = next_highest_value + 1
                last_term = inventory[0]
                total_profit += (first_term + last_term) * price_difference // 2 * item_count
                inventory[0] = next_highest_value
            orders -= potential_orders
            total_profit %= self.x
        return total_profit
