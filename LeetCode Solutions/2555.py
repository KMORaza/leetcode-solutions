class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        if k == 0:
            max_single = 0
            i = 0
            while i < n:
                j = i
                while j < n and prizePositions[j] == prizePositions[i]:
                    j += 1
                max_single = max(max_single, j - i)
                i = j

            if max_single >= n:
                return n
            else:
                i = 0
                max_two = 0
                while i < n:
                    j = i
                    while j < n and prizePositions[j] == prizePositions[i]:
                        j += 1
                    first_len = j - i
                    next_i = j
                    while next_i < n and prizePositions[next_i] == prizePositions[j - 1]:
                        next_i += 1
                    if next_i < n:
                        next_j = next_i
                        while next_j < n and prizePositions[next_j] == prizePositions[next_i]:
                            next_j += 1
                        second_len = next_j - next_i
                        max_two = max(max_two, first_len + second_len)
                    else:
                        max_two = max(max_two, first_len)
                    i = j
                return max_two

        left = [0] * n
        j = 0
        for i in range(n):
            while prizePositions[i] - prizePositions[j] > k:
                j += 1
            left[i] = i - j + 1
            if i > 0:
                left[i] = max(left[i], left[i - 1])

        max_win = 0
        j = n - 1
        for i in range(n - 1, -1, -1):
            while j >= 0 and prizePositions[j] - prizePositions[i] > k:
                j -= 1

            second_segment = j - i + 1
            first_segment = left[i - 1] if i > 0 else 0
            max_win = max(max_win, first_segment + second_segment)

        return max_win