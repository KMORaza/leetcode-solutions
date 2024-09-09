class Solution:
    def flipgame(self, fronts, backs):
        k = 2001
        output = k
        same = set()
        for front, back in zip(fronts, backs):
            if front == back:
                same.add(front)
        for front in fronts:
            if front not in same:
                output = min(output, front)
        for back in backs:
            if back not in same:
                output = min(output, back)
        return 0 if output == k else output
