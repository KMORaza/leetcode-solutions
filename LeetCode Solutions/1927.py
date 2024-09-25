class Solution:
    def sumGame(self, game_string: str) -> bool:
        string_length = len(game_string)
        score_difference = 0.0
        for first_half_index in range(string_length // 2):
            score_difference += self.determine_value(game_string[first_half_index])
        for second_half_index in range(string_length // 2, string_length):
            score_difference -= self.determine_value(game_string[second_half_index])
        return score_difference != 0.0
    def determine_value(self, char: str) -> float:
        return 4.5 if char == '?' else int(char)
