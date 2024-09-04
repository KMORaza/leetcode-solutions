class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = list(map(int, version1.split('.')))
        revisions2 = list(map(int, version2.split('.')))
        max_length = max(len(revisions1), len(revisions2))
        revisions1.extend([0] * (max_length - len(revisions1)))
        revisions2.extend([0] * (max_length - len(revisions2)))
        for rev1, rev2 in zip(revisions1, revisions2):
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        return 0
