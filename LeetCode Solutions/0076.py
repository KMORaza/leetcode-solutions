class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        if not t or not s:
            return ""
        t_count = Counter(t)
        window_count = defaultdict(int)
        required = len(t_count)
        formed = 0
        l, r = 0, 0
        min_len = float('inf')
        min_window = ""
        while r < len(s):
            character = s[r]
            window_count[character] += 1
            if character in t_count and window_count[character] == t_count[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]
                window_count[character] -= 1
                if character in t_count and window_count[character] < t_count[character]:
                    formed -= 1
                l += 1
            r += 1
        return min_window
