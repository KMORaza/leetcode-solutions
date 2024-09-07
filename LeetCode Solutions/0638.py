from typing import List, Tuple, Dict
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo: Dict[Tuple[int], int] = {}
        def dp(current_needs: Tuple[int]) -> int:
            if all(x == 0 for x in current_needs):
                return 0
            if current_needs in memo:
                return memo[current_needs]
            min_cost = float('inf')
            direct_cost = sum(price[i] * current_needs[i] for i in range(len(needs)))
            min_cost = min(min_cost, direct_cost)
            for offer in special:
                offer_cost = offer[-1]
                offer_items = offer[:-1]
                new_needs = []
                valid_offer = True
                for i in range(len(needs)):
                    if current_needs[i] < offer_items[i]:
                        valid_offer = False
                        break
                    new_needs.append(current_needs[i] - offer_items[i])
                if valid_offer:
                    min_cost = min(min_cost, offer_cost + dp(tuple(new_needs)))
            memo[current_needs] = min_cost
            return min_cost
        return dp(tuple(needs))
