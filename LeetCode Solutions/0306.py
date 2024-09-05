class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid_number(s: str) -> bool:
            return not (len(s) > 1 and s[0] == '0')
        n = len(num)
        for i in range(1, n // 2 + 1):
            for j in range(i + 1, min(i + (n - i) // 2 + 1, n)):
                num1 = num[:i]
                num2 = num[i:j]
                if not is_valid_number(num1) or not is_valid_number(num2):
                    continue
                k = j
                while k < n:
                    num3 = str(int(num1) + int(num2))
                    if not num.startswith(num3, k):
                        break
                    k += len(num3)
                    num1, num2 = num2, num3
                if k == n:
                    return True
        return False