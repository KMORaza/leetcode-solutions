class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        val_to_indices = {}
        n = len(s)

        for i in range(n):
            if s[i] == '0':
                if 0 not in val_to_indices:
                    val_to_indices[0] = [i, i]
                continue

            num = 0
            for j in range(i, min(i + 32, n)):
                num = (num << 1) | int(s[j])
                if num > 2 ** 32:
                    break
                if num not in val_to_indices:
                    val_to_indices[num] = [i, j]

        result = []
        for first, second in queries:
            target = first ^ second
            if target in val_to_indices:
                result.append(val_to_indices[target])
            else:
                result.append([-1, -1])

        return result