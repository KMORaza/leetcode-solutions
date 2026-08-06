class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        last_g = last_p = last_m = -1
        total_garbage_time = 0

        for i in range(n):
            total_garbage_time += len(garbage[i])
            if 'G' in garbage[i]:
                last_g = i
            if 'P' in garbage[i]:
                last_p = i
            if 'M' in garbage[i]:
                last_m = i

        prefix_travel = [0]
        for t in travel:
            prefix_travel.append(prefix_travel[-1] + t)

        result = total_garbage_time
        if last_g > 0:
            result += prefix_travel[last_g]
        if last_p > 0:
            result += prefix_travel[last_p]
        if last_m > 0:
            result += prefix_travel[last_m]

        return result