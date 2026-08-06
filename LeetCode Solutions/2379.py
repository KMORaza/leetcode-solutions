class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_changes = float('inf')

        for i in range(n - k + 1):
            window = blocks[i:i + k]
            changes_needed = window.count('W')
            min_changes = min(min_changes, changes_needed)

        return min_changes