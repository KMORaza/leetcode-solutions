class Solution:
    def minTimeToType(self, word: str) -> int:
        time = len(word)
        current_position = 0
        for char in word:
            target_position = ord(char) - ord('a')
            distance = abs(target_position - current_position)
            time += min(distance, 26 - distance)
            current_position = target_position
        return time