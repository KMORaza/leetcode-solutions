class Solution:
    def pyramidTransition(self, bottom: str, allowed: list) -> bool:
        from collections import defaultdict
        allowed_set = set(allowed)
        transition_map = defaultdict(set)
        for pattern in allowed_set:
            transition_map[(pattern[0], pattern[1])].add(pattern[2])
        memo = {}
        def can_build_pyramid(bottom):
            if len(bottom) == 1:
                return True
            if bottom in memo:
                return memo[bottom]
            n = len(bottom)
            next_rows = []
            def generate_next_rows(current_row, index):
                if index == n - 1:
                    if len(current_row) == n - 1:
                        next_rows.append(''.join(current_row))
                    return
                left = bottom[index]
                right = bottom[index + 1]
                if (left, right) in transition_map:
                    for top_block in transition_map[(left, right)]:
                        current_row.append(top_block)
                        generate_next_rows(current_row, index + 1)
                        current_row.pop()
            generate_next_rows([], 0)
            for next_row in next_rows:
                if can_build_pyramid(next_row):
                    memo[bottom] = True
                    return True
            memo[bottom] = False
            return False
        return can_build_pyramid(bottom)
