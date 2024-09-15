from collections import deque
from enum import Enum
class CatAndMouse(Enum):
    tied = 0
    mouse_is_winner = 1
    cat_is_winner = 2
class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        outcome = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        out_degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        q = deque()
        for cat in range(n):
            for mouse in range(n):
                out_degree[cat][mouse][0] = len(graph[mouse])
                out_degree[cat][mouse][1] = len(graph[cat]) - (1 if 0 in graph[cat] else 0)
        for cat in range(1, n):
            for move in range(2):
                outcome[cat][0][move] = CatAndMouse.mouse_is_winner.value
                q.append((cat, 0, move, CatAndMouse.mouse_is_winner.value))
                outcome[cat][cat][move] = CatAndMouse.cat_is_winner.value
                q.append((cat, cat, move, CatAndMouse.cat_is_winner.value))
        while q:
            cat, mouse, move, state = q.popleft()
            if cat == 2 and mouse == 1 and move == 0:
                return state
            prev_move = 1 - move
            for prev in graph[mouse if prev_move == 0 else cat]:
                prev_cat = cat if prev_move == 0 else prev
                if prev_cat == 0:
                    continue
                prev_mouse = prev if prev_move == 0 else mouse
                if outcome[prev_cat][prev_mouse][prev_move] > 0:
                    continue
                out_degree[prev_cat][prev_mouse][prev_move] -= 1
                if (prev_move == 0 and state == CatAndMouse.mouse_is_winner.value or
                    prev_move == 1 and state == CatAndMouse.cat_is_winner.value or
                    out_degree[prev_cat][prev_mouse][prev_move] == 0):
                    outcome[prev_cat][prev_mouse][prev_move] = state
                    q.append((prev_cat, prev_mouse, prev_move, state))
        return outcome[2][1][0]
