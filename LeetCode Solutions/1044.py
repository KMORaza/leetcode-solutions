class Solution:
    def longestDupSubstring(self, s: str) -> str:
        length = len(s)
        power_values = [0] * length
        best_start_index = -1
        lower_bound, upper_bound = 1, length
        power_values[0] = 1
        for i in range(1, length):
            power_values[i] = (power_values[i - 1] * Solution.BASE) % Solution.MODULO
        while lower_bound < upper_bound:
            mid_length = (lower_bound + upper_bound) // 2
            start_index = self.find_duplicate_start(s, mid_length, power_values)
            if start_index == -1:
                upper_bound = mid_length
            else:
                best_start_index = start_index
                lower_bound = mid_length + 1
        if best_start_index == -1:
            return ""
        if self.find_duplicate_start(s, lower_bound, power_values) == -1:
            return s[best_start_index:best_start_index + lower_bound - 1]
        return s[best_start_index:best_start_index + lower_bound]
    BASE = 26
    MODULO = 1_000_000_007
    @staticmethod
    def char_to_value(c: str) -> int:
        return ord(c) - ord('a')
    def find_duplicate_start(self, s: str, length: int, power_values: list[int]) -> int:
        hash_map = {}
        current_hash = 0
        for i in range(length):
            current_hash = (current_hash * Solution.BASE + self.char_to_value(s[i])) % Solution.MODULO
        hash_map[current_hash] = [0]
        for i in range(length, len(s)):
            start_index = i - length + 1
            current_hash = (current_hash - power_values[length - 1] * self.char_to_value(s[i - length])) % Solution.MODULO
            current_hash = (current_hash + Solution.MODULO) % Solution.MODULO
            current_hash = (current_hash * Solution.BASE + self.char_to_value(s[i])) % Solution.MODULO
            if current_hash in hash_map:
                current_substring = s[start_index:start_index + length]
                for start in hash_map[current_hash]:
                    if s[start:start + length] == current_substring:
                        return start_index
            hash_map[current_hash] = hash_map.get(current_hash, [])
            hash_map[current_hash].append(start_index)
        return -1
