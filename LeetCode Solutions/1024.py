from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))
        current_end = 0
        max_end = 0
        clips_count = 0
        i = 0
        n = len(clips)
        while current_end < time:
            while i < n and clips[i][0] <= current_end:
                max_end = max(max_end, clips[i][1])
                i += 1
            if max_end <= current_end:
                return -1
            current_end = max_end
            clips_count += 1
        return clips_count
