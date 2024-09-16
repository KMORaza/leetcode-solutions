from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        b_count = count.get('b', 0)
        a_count = count.get('a', 0)
        l_count = count.get('l', 0) // 2
        o_count = count.get('o', 0) // 2
        n_count = count.get('n', 0)
        return min(b_count, a_count, l_count, o_count, n_count)
