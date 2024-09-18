from collections import defaultdict
import bisect
from typing import List
class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(list)
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweets:
            return []
        times = self.tweets[tweetName]
        interval = {
            'minute': 60,
            'hour': 3600,
            'day': 86400
        }[freq]
        result = [0] * ((endTime - startTime) // interval + 1)
        for time in times:
            if startTime <= time <= endTime:
                index = (time - startTime) // interval
                result[index] += 1
        return result
