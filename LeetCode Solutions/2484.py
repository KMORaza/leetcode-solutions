class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        if n < 5:
            return 0

        suff2 = [[[0] * 10 for _ in range(10)] for _ in range(n + 1)]
        scnt = [0] * 10
        for i in range(n - 1, -1, -1):
            d = int(s[i])
            for d2 in range(10):
                suff2[i][d][d2] = (suff2[i][d][d2] + scnt[d2]) % MOD
            for d1 in range(10):
                for d2 in range(10):
                    suff2[i][d1][d2] = (suff2[i][d1][d2] + suff2[i + 1][d1][d2]) % MOD
            scnt[d] += 1

        pref2 = [[0] * 10 for _ in range(10)]
        cnt = [0] * 10
        ans = 0

        d0 = int(s[0])
        cnt[d0] += 1
        d1 = int(s[1])
        for d in range(10):
            pref2[d][d1] = (pref2[d][d1] + cnt[d]) % MOD
        cnt[d1] += 1

        for k in range(2, n - 2):
            total = 0
            for a in range(10):
                for b in range(10):
                    total = (total + pref2[a][b] * suff2[k + 1][b][a]) % MOD
            ans = (ans + total) % MOD

            dk = int(s[k])
            for d in range(10):
                pref2[d][dk] = (pref2[d][dk] + cnt[d]) % MOD
            cnt[dk] += 1

        return ans