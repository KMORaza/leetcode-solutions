class Solution:
    def numberOfWays(self, layout: str) -> int:
        total_ways = 1
        last_position = -1
        seat_total = 0
        for pos in range(len(layout)):
            if layout[pos] == 'S':
                seat_total += 1
                if seat_total > 2 and seat_total % 2 == 1:
                    total_ways = (total_ways * (pos - last_position)) % (10**9+7)
                last_position = pos
        return int(total_ways) if seat_total > 1 and seat_total % 2 == 0 else 0