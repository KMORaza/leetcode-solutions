from collections import defaultdict, Counter
import sys
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counts = [Counter(sticker) for sticker in stickers]
        INF = float('inf')
        dp = [INF] * (1 << len(target))
        dp[0] = 0
        target_len = len(target)
        target_map = {ch: idx for idx, ch in enumerate(target)}
        for mask in range(1 << target_len):
            if dp[mask] == INF:
                continue
            for sticker in sticker_counts:
                new_mask = mask
                for ch, count in sticker.items():
                    if ch in target_map:
                        pos = target_map[ch]
                        for i in range(target_len):
                            if mask & (1 << i) == 0 and target[i] == ch:
                                if count > 0:
                                    count -= 1
                                    new_mask |= (1 << i)
                                    if count == 0:
                                        break
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
        final_mask = (1 << target_len) - 1
        return dp[final_mask] if dp[final_mask] != INF else -1
