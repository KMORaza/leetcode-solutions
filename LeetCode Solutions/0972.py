class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        return abs(self.value(S) - self.value(T)) < 1E-9
    def value(self, S: str) -> float:
        i = S.find('(')
        if i > 0:
            base = S[:i]
            rep = S[i + 1:-1]
            base += rep * 20
            return float(base)
        else:
            return float(S)
