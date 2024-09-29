class Solution:
    def subStrHash(self, input_str: str, base_value: int, modulus: int, substring_size: int, target_hash_value: int) -> str:
        exponent_tracker = 1
        current_checksum = 0
        optimal_index = -1
        for idx in range(len(input_str) - 1, -1, -1):
            current_checksum = (current_checksum * base_value + self.character_to_numeric(input_str[idx])) % modulus
            if idx + substring_size < len(input_str):
                current_checksum = (current_checksum - self.character_to_numeric(input_str[idx + substring_size]) * exponent_tracker % modulus + modulus) % modulus
            else:
                exponent_tracker = exponent_tracker * base_value % modulus
            if current_checksum == target_hash_value:
                optimal_index = idx
        return input_str[optimal_index:optimal_index + substring_size]
    def character_to_numeric(self, char: str) -> int:
        return ord(char) - ord('a') + 1