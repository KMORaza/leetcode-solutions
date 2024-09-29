class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_length = 0
        left = 0
        count_T = 0
        count_F = 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                count_T += 1
            else:
                count_F += 1
            while min(count_T, count_F) > k:
                if answerKey[left] == 'T':
                    count_T -= 1
                else:
                    count_F -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
