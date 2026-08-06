class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        from collections import Counter

        count1 = Counter(word1)
        count2 = Counter(word2)

        for c1 in count1:
            for c2 in count2:
                # Simulate swapping c1 from word1 with c2 from word2
                new_count1 = count1.copy()
                new_count2 = count2.copy()

                # Remove c1 from word1 and add c2
                new_count1[c1] -= 1
                if new_count1[c1] == 0:
                    del new_count1[c1]
                new_count1[c2] = new_count1.get(c2, 0) + 1

                # Remove c2 from word2 and add c1
                new_count2[c2] -= 1
                if new_count2[c2] == 0:
                    del new_count2[c2]
                new_count2[c1] = new_count2.get(c1, 0) + 1

                if len(new_count1) == len(new_count2):
                    return True

        return False