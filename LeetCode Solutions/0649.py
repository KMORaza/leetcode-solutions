from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()
        for i, char in enumerate(senate):
            if char == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)
        while radiant_queue and dire_queue:
            radiant_index = radiant_queue.popleft()
            dire_index = dire_queue.popleft()
            if radiant_index < dire_index:
                radiant_queue.append(radiant_index + len(senate))
            else:
                dire_queue.append(dire_index + len(senate))
        if radiant_queue:
            return "Radiant"
        else:
            return "Dire"
