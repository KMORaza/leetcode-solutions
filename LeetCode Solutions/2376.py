class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        k = len(s)

        # Count all special numbers with fewer digits than n
        result = 0
        for i in range(1, k):
            count = 9
            for j in range(i - 1):
                count *= (9 - j)
            result += count

        # Count special numbers with same number of digits as n and <= n
        used = [False] * 10
        for i in range(k):
            smaller_count = 0
            for digit in range(0 if i > 0 else 1, int(s[i])):
                if not used[digit]:
                    smaller_count += 1

            remaining_positions = k - i - 1
            available_digits = 10 - i - 1
            temp = smaller_count
            for j in range(remaining_positions):
                temp *= (available_digits - j)
            result += temp

            if used[int(s[i])]:
                break
            used[int(s[i])] = True
        else:
            result += 1

        return result