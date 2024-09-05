from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.tweet_counter = 0
        self.user_tweets = defaultdict(list)
        self.following = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_counter += 1
        self.user_tweets[userId].append((self.tweet_counter, tweetId))
    def getNewsFeed(self, userId: int) -> list:
        tweets = []
        for timestamp, tweetId in self.user_tweets[userId]:
            tweets.append((timestamp, tweetId))
        for followee in self.following[userId]:
            tweets.extend(self.user_tweets[followee])
        tweets.sort(reverse=True)
        return [tweetId for _, tweetId in tweets[:10]]
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId] and followerId != followeeId:
            self.following[followerId].remove(followeeId)
