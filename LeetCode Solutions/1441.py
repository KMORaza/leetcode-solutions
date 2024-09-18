class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        current = 0
        for i in range(1, n + 1):
            res.append("Push")
            if current < len(target) and target[current] == i:
                current += 1
            else:
                res.append("Pop")
            if current == len(target):
                break
        return res
