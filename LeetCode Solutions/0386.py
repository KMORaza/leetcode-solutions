class Solution:
    def lexicalOrder(self, n: int):
        result = []
        def dfs(current):
            if current > n:
                return
            if current != 0:
                result.append(current)
            for i in range(10):
                next_number = current * 10 + i
                if next_number > n:
                    break
                dfs(next_number)
        for i in range(1, 10):
            dfs(i)
        return result
