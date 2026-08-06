class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def hamming_distance(s1, s2):
            if len(s1) != len(s2):
                return float('inf')
            dist = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    dist += 1
                    if dist > 2:
                        return dist
            return dist

        result = []
        for query in queries:
            found = False
            for word in dictionary:
                if hamming_distance(query, word) <= 2:
                    result.append(query)
                    found = True
                    break

        return result