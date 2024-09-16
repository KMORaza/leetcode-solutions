from typing import List, Dict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        def parse_transaction(t: str) -> 'TransactionAccount':
            parts = t.split(',')
            return TransactionAccount(parts[0], int(parts[1]), int(parts[2]), parts[3])
        class TransactionAccount:
            def __init__(self, name: str, time: int, amount: int, city: str):
                self.name = name
                self.time = time
                self.amount = amount
                self.city = city
        result = []
        name_to_transactions: Dict[str, List[TransactionAccount]] = {}
        for t in transactions:
            trans = parse_transaction(t)
            if trans.name not in name_to_transactions:
                name_to_transactions[trans.name] = []
            name_to_transactions[trans.name].append(trans)
        for t in transactions:
            current_trans = parse_transaction(t)
            if current_trans.amount > 1000:
                result.append(t)
            elif current_trans.name in name_to_transactions:
                for trans in name_to_transactions[current_trans.name]:
                    if abs(trans.time - current_trans.time) <= 60 and trans.city != current_trans.city:
                        result.append(t)
                        break
        return result