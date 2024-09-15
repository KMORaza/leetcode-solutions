class Solution:
    def countRoutes(self, cities, origin, destination, maxFuel):
        dp = [[None] * (maxFuel + 1) for _ in range(len(cities))]
        return self._calculateRoutes(cities, origin, destination, maxFuel, dp)
    def _calculateRoutes(self, cities, current, destination, remainingFuel, dp):
        X = 1000000007
        if remainingFuel < 0:
            return 0
        if dp[current][remainingFuel] is not None:
            return dp[current][remainingFuel]
        result = 1 if current == destination else 0
        for next_city in range(len(cities)):
            if next_city != current:
                result += self._calculateRoutes(cities, next_city, destination, remainingFuel - abs(cities[current] - cities[next_city]), dp)
                result %= X
        dp[current][remainingFuel] = result
        return result
