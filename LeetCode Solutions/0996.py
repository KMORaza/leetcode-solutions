import math
from collections import Counter
class Solution:
    def numSquarefulPerms(self, A):
        def is_square(n):
            if n < 0:
                return False
            root = int(math.sqrt(n))
            return root * root == n
        def backtrack(path, counter):
            if len(path) == len(A):
                self.result += 1
                return
            for num in counter:
                if counter[num] > 0:
                    if not path or is_square(path[-1] + num):
                        counter[num] -= 1
                        path.append(num)
                        backtrack(path, counter)
                        path.pop()
                        counter[num] += 1
        self.result = 0
        counter = Counter(A)
        backtrack([], counter)
        return self.result
