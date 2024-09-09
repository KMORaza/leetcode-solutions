from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        def neighbors(state):
            for i in range(4):
                digit = int(state[i])
                for d in [-1, 1]:
                    new_digit = (digit + d) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    yield new_state
        queue = deque(["0000"])
        visited = set(["0000"])
        moves = 0
        while queue:
            for _ in range(len(queue)):
                current_state = queue.popleft()
                if current_state == target:
                    return moves
                for next_state in neighbors(current_state):
                    if next_state not in visited and next_state not in deadends_set:
                        visited.add(next_state)
                        queue.append(next_state)
            moves += 1
        return -1
