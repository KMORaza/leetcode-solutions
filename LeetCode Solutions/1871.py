class Solution:
    def canReach(self, input_str: str, jump_min: int, jump_max: int) -> bool:
        reachable_count = 0
        reachable = [False] * len(input_str)
        reachable[0] = True
        for index in range(jump_min, len(input_str)):
            reachable_count += 1 if reachable[index - jump_min] else 0
            if index - jump_max - 1 >= 0:
                reachable_count -= 1 if reachable[index - jump_max - 1] else 0
            reachable[index] = reachable_count > 0 and input_str[index] == '0'
        return reachable[-1]
