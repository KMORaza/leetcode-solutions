class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        presses = min(presses, 4)
        unique_states = set()
        def apply_buttons(buttons):
            state = [1] * n
            for button in buttons:
                if button == 1:
                    state = [1 - x for x in state]
                elif button == 2:
                    state = [(1 - state[i] if (i + 1) % 2 == 0 else state[i]) for i in range(n)]
                elif button == 3:
                    state = [(1 - state[i] if (i + 1) % 2 != 0 else state[i]) for i in range(n)]
                elif button == 4:
                    state = [(1 - state[i] if (i + 1) % 3 == 1 else state[i]) for i in range(n)]
            return tuple(state)
        from itertools import product
        for combo in product(range(1, 5), repeat=presses):
            unique_states.add(apply_buttons(combo))
        return len(unique_states)
