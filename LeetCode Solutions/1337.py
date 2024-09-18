class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [x[1] for x in sorted(((sum(row), i) for i, row in enumerate(mat)), key=lambda x: (x[0], x[1]))[:k]]
