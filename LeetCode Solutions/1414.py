class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1, 2]
        while True:
            next_fib = fibs[-1] + fibs[-2]
            if next_fib > k:
                break
            fibs.append(next_fib)
        count = 0
        index = len(fibs) - 1
        while k > 0:
            while fibs[index] > k:
                index -= 1
            k -= fibs[index]
            count += 1
        return count
