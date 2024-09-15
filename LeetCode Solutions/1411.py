class Solution:
    def numOfWays(self, n: int) -> int:
        X = 1000000007
        patternCount2 = 6
        patternCount3 = 6
        for _ in range(1, n):
            nextPatternCount2 = patternCount2 * 3 + patternCount3 * 2
            nextPatternCount3 = patternCount2 * 2 + patternCount3 * 2
            patternCount2 = nextPatternCount2 % X
            patternCount3 = nextPatternCount3 % X
        return (patternCount2 + patternCount3) % X
