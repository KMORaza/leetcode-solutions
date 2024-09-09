class Solution:
    def intersectionSizeTwo(self, intervals):
        output = 0
        mx = -1
        second_max = -1
        intervals.sort(key=lambda x: (x[1], -x[0]))
        for interval in intervals:
            a, b = interval
            if mx >= a and second_max >= a:
                continue
            if mx >= a:
                second_max = mx
                mx = b
                output += 1
            else:
                mx = b
                second_max = b - 1
                output += 2
        return output
