from typing import List
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        total_values = [(a + b, a, b) for a, b in zip(aliceValues, bobValues)]
        total_values.sort(reverse=True, key=lambda x: x[0])
        alice_score, bob_score = 0, 0
        for i in range(len(total_values)):
            if i % 2 == 0:
                alice_score += total_values[i][1]
            else:
                bob_score += total_values[i][2]
        if alice_score > bob_score:
            return 1
        elif bob_score > alice_score:
            return -1
        else:
            return 0
