class Solution:
    def oddEvenJumps(self, A):
        def make_sorted_indices(arr):
            sorted_indices = sorted(range(len(arr)), key=lambda x: arr[x])
            return sorted_indices
        def make_even_sorted_indices(arr):
            sorted_indices = sorted(range(len(arr)), key=lambda x: (-arr[x], x))
            return sorted_indices
        def next_jump(sorted_indices, arr):
            next_jump = [-1] * len(arr)
            stack = []
            for index in sorted_indices:
                while stack and stack[-1] < index:
                    next_jump[stack.pop()] = index
                stack.append(index)
            return next_jump
        n = len(A)
        if n == 0:
            return 0
        odd_jump = next_jump(make_sorted_indices(A), A)
        even_jump = next_jump(make_even_sorted_indices(A), A)
        can_reach_end_odd = [False] * n
        can_reach_end_even = [False] * n
        can_reach_end_odd[-1] = True
        can_reach_end_even[-1] = True
        for i in range(n - 2, -1, -1):
            if odd_jump[i] != -1:
                can_reach_end_odd[i] = can_reach_end_even[odd_jump[i]]
            if even_jump[i] != -1:
                can_reach_end_even[i] = can_reach_end_odd[even_jump[i]]
        return sum(can_reach_end_odd)
