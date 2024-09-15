from collections import deque
class Solution:
    def boxDelivering(self, items, portCount, boxLimit, weightLimit):
        itemCount = len(items)
        weightCumulative = [0] * (itemCount + 1)
        portChanges = [0] * itemCount
        for idx in range(itemCount):
            port = items[idx][0]
            weight = items[idx][1]
            weightCumulative[idx + 1] = weightCumulative[idx] + weight
            if idx < itemCount - 1:
                portChanges[idx + 1] = portChanges[idx] + (1 if port != items[idx + 1][0] else 0)
        minDeliveries = [float('inf')] * (itemCount + 1)
        minDeliveries[0] = 0
        deq = deque([0])
        for idx in range(1, itemCount + 1):
            while deq and (idx - deq[0] > boxLimit or weightCumulative[idx] - weightCumulative[deq[0]] > weightLimit):
                deq.popleft()
            if deq:
                minDeliveries[idx] = portChanges[idx - 1] + minDeliveries[deq[0]] - portChanges[deq[0]] + 2
            if idx < itemCount:
                while deq and minDeliveries[deq[-1]] - portChanges[deq[-1]] >= minDeliveries[idx] - portChanges[idx]:
                    deq.pop()
                deq.append(idx)
        return minDeliveries[itemCount]
