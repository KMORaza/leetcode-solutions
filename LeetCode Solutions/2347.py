class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        from collections import Counter
        rank_counts = Counter(ranks)
        max_count = max(rank_counts.values())

        if max_count >= 3:
            return "Three of a Kind"
        elif max_count >= 2:
            return "Pair"
        else:
            return "High Card"