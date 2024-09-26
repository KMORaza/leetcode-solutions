class Solution:
    def minSessions(self, a, b):
        for c in range(1, len(a) + 1):
            if self.d(a, 0, [0] * c, b):
                return c
        raise RuntimeError("Unable to allocate tasks")
    def d(self, a, e, f, b):
        if e == len(a):
            return True
        for g in range(len(f)):
            if f[g] + a[e] > b:
                continue
            f[g] += a[e]
            if self.d(a, e + 1, f, b):
                return True
            f[g] -= a[e]
            if f[g] == 0:
                return False
        return False
