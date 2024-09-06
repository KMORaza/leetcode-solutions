class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing = self.getMissing(password)
        replaces = 0
        oneSeq = 0
        twoSeq = 0
        i = 2
        while i < n:
            if (password[i] == password[i - 1] and
                password[i - 1] == password[i - 2]):
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                replaces += length // 3
                if length % 3 == 0:
                    oneSeq += 1
                elif length % 3 == 1:
                    twoSeq += 1
            else:
                i += 1
        if n < 6:
            return max(6 - n, missing)
        elif n <= 20:
            return max(replaces, missing)
        else:
            deletes = n - 20
            replaces -= min(oneSeq, deletes)
            replaces -= min(max(deletes - oneSeq, 0), twoSeq * 2) // 2
            replaces -= max(deletes - oneSeq - twoSeq * 2, 0) // 3
            return deletes + max(replaces, missing)
    def getMissing(self, password: str) -> int:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        return 3 - (has_upper + has_lower + has_digit)