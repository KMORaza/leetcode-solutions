from typing import List
import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_orders = []
        sell_orders = []
        for price, amount, order_type in orders:
            if order_type == 0:
                heapq.heappush(buy_orders, (-price, amount))
            else:
                heapq.heappush(sell_orders, (price, amount))
            while buy_orders and sell_orders:
                max_buy_price, buy_amount = buy_orders[0]
                min_sell_price, sell_amount = sell_orders[0]
                if -max_buy_price >= min_sell_price:
                    matched_amount = min(buy_amount, sell_amount)
                    buy_amount -= matched_amount
                    sell_amount -= matched_amount
                    if buy_amount == 0:
                        heapq.heappop(buy_orders)
                    else:
                        buy_orders[0] = (-(-max_buy_price), buy_amount)
                    if sell_amount == 0:
                        heapq.heappop(sell_orders)
                    else:
                        sell_orders[0] = (min_sell_price, sell_amount)
                else:
                    break
        total_backlog = 0
        for _, amount in buy_orders:
            total_backlog += amount
        for _, amount in sell_orders:
            total_backlog += amount
        return total_backlog % (10**9 + 7)
