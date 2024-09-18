class Solution:
    def minSwaps(self, a):
        b = len(a)
        c = 0
        d = [0] * b
        for e in range(b):
            d[e] = self.f(a[e])
        for g in range(b):
            h = b - 1 - g
            i = self.j(d, g, h)
            if i == -1:
                return -1
            for k in range(i, g, -1):
                d[k] = d[k - 1]
            c += i - g
        return c
    def f(self, m):
        for n in range(len(m) - 1, -1, -1):
            if m[n] == 1:
                return len(m) - n - 1
        return len(m)
    def j(self, p, q, r):
        for s in range(q, len(p)):
            if p[s] >= r:
                return s
        return -1
