from collections import defaultdict
from typing import List
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_count = defaultdict(int)
        for message, sender in zip(messages, senders):
            word_count[sender] += len(message.split())
        max_count = 0
        result_sender = ""
        for sender, count in word_count.items():
            if count > max_count or (count == max_count and sender > result_sender):
                max_count = count
                result_sender = sender
        return result_sender
