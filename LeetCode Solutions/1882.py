import heapq
class Solution:
    def assignTasks(self, weightList: list[int], durationList: list[int]) -> list[int]:
        taskCount = len(durationList)
        serverCount = len(weightList)
        freeServers = []
        activeServers = []
        for serverIndex in range(serverCount):
            heapq.heappush(freeServers, (weightList[serverIndex], serverIndex))
        taskAssignments = [-1] * taskCount
        for timeUnit in range(taskCount):
            currentDuration = durationList[timeUnit]
            while activeServers and activeServers[0][0] <= timeUnit:
                endTime, weight, index = heapq.heappop(activeServers)
                heapq.heappush(freeServers, (weight, index))
            if freeServers:
                weight, index = heapq.heappop(freeServers)
                taskAssignments[timeUnit] = index
                heapq.heappush(activeServers, (timeUnit + currentDuration, weight, index))
            else:
                endTime, weight, index = heapq.heappop(activeServers)
                taskAssignments[timeUnit] = index
                heapq.heappush(activeServers, (endTime + currentDuration, weight, index))
        return taskAssignments
