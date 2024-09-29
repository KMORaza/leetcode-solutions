class Solution:
    movement_patterns = {
        "rook": [[1, 0], [-1, 0], [0, 1], [0, -1]],
        "bishop": [[1, 1], [1, -1], [-1, 1], [-1, -1]],
        "queen": [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]],
    }
    def countCombinations(self, chess_pieces, initial_positions):
        total_pieces = len(chess_pieces)
        seen_board_states = set()
        all_move_variations = []
        self.collect_move_variations(chess_pieces, 0, [], all_move_variations)
        for move_variation in all_move_variations:
            self.explore_board_states(initial_positions, total_pieces, move_variation, (1 << total_pieces) - 1, seen_board_states)
        return len(seen_board_states)
    def collect_move_variations(self, chess_pieces, piece_index, current_moves, all_move_variations):
        if piece_index == len(chess_pieces):
            all_move_variations.append(list(current_moves))
            return
        for move in self.movement_patterns[chess_pieces[piece_index]]:
            current_moves.append(move)
            self.collect_move_variations(chess_pieces, piece_index + 1, current_moves, all_move_variations)
            current_moves.pop()
    def explore_board_states(self, current_board_state, total_pieces, move_variation, mask_of_active_pieces, seen_board_states):
        if mask_of_active_pieces == 0:
            return
        seen_board_states.add(self.generate_board_signature(current_board_state))
        for new_mask in range(1, 1 << total_pieces):
            if (mask_of_active_pieces & new_mask) != new_mask:
                continue
            updated_board = [row[:] for row in current_board_state]
            for index in range(total_pieces):
                if (new_mask >> index) & 1:
                    updated_board[index][0] += move_variation[index][0]
                    updated_board[index][1] += move_variation[index][1]
            if self.count_distinct_positions(updated_board) < total_pieces:
                continue
            if all(1 <= square[0] <= 8 and 1 <= square[1] <= 8 for square in updated_board):
                self.explore_board_states(updated_board, total_pieces, move_variation, new_mask, seen_board_states)
    def generate_board_signature(self, current_board_state):
        signature_value = 0
        for square in current_board_state:
            signature_value = (signature_value * 64) + ((square[0] - 1) << 3) + (square[1] - 1)
        return signature_value
    def count_distinct_positions(self, current_board_state):
        unique_coordinates = set()
        for square in current_board_state:
            unique_coordinates.add(square[0] * 8 + square[1])
        return len(unique_coordinates)
