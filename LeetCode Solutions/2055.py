class Solution:
    def platesBetweenCandles(self, string_input: str, query_pairs: list[list[int]]) -> list[int]:
        output = [0] * len(query_pairs)
        candle_positions = []
        for char_index in range(len(string_input)):
            if string_input[char_index] == '|':
                candle_positions.append(char_index)
        for q_index, (query_start, query_end) in enumerate(query_pairs):
            left_candle = self.findFirstPosition(candle_positions, query_start)
            right_candle = self.findFirstPosition(candle_positions, query_end + 1) - 1
            if left_candle < right_candle:
                space_between = candle_positions[right_candle] - candle_positions[left_candle] + 1
                total_candles = right_candle - left_candle + 1
                output[q_index] = space_between - total_candles
        return output
    def findFirstPosition(self, candle_positions: list[int], target_value: int) -> int:
        from bisect import bisect_left
        position = bisect_left(candle_positions, target_value)
        return position
