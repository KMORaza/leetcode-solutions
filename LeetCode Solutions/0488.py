class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        from collections import Counter
        def remove_consecutive(board):
            i = 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1
                if j - i >= 3:
                    return remove_consecutive(board[:i] + board[j:])
                i = j
            return board
        def dfs(board, hand):
            board = remove_consecutive(board)
            if not board:
                return 0
            if not hand:
                return float('inf')
            memo_key = (board, tuple(sorted(hand)))
            if memo_key in memo:
                return memo[memo_key]
            min_steps = float('inf')
            hand_counter = Counter(hand)
            for i in range(len(board) + 1):
                for color in hand_counter:
                    if hand_counter[color] > 0:
                        new_hand = hand_counter.copy()
                        new_hand[color] -= 1
                        new_hand_str = ''.join(color * new_hand[color] for color in sorted(new_hand))
                        new_board = board[:i] + color + board[i:]
                        steps = dfs(remove_consecutive(new_board), new_hand_str)
                        if steps != float('inf'):
                            min_steps = min(min_steps, steps + 1)
            memo[memo_key] = min_steps
            return min_steps
        memo = {}
        result = dfs(board, hand)
        return result if result != float('inf') else -1