class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = 0
        mask_count = {0: 1}
        current_mask = 0
        for char in word:
            current_mask ^= (1 << (ord(char) - ord('a')))
            count += mask_count.get(current_mask, 0)
            for i in range(10):
                count += mask_count.get(current_mask ^ (1 << i), 0)
            mask_count[current_mask] = mask_count.get(current_mask, 0) + 1
        return count
