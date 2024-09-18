from typing import List
from collections import deque, Counter
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque([(id, 0)])
        visited = set([id])
        video_count = Counter()
        while queue:
            user, curr_level = queue.popleft()
            if curr_level == level:
                for video in watchedVideos[user]:
                    video_count[video] += 1
            elif curr_level < level:
                for friend in friends[user]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append((friend, curr_level + 1))
        sorted_videos = sorted(video_count.keys(), key=lambda video: (video_count[video], video))
        return sorted_videos
