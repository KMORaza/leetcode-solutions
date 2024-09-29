class Solution:
    def maxTwoEvents(self, schedule):
        schedule.sort(key=lambda x: x[0])
        eventCount = len(schedule)
        maxValueAfterEvent = [0] * (eventCount + 1)
        for index in range(eventCount - 1, -1, -1):
            maxValueAfterEvent[index] = max(maxValueAfterEvent[index + 1], schedule[index][2])
        highestValue = 0
        for current in schedule:
            currentEventValue = current[2]
            low, high = 0, eventCount
            while low < high:
                midPoint = (low + high) // 2
                if schedule[midPoint][0] > current[1]:
                    high = midPoint
                else:
                    low = midPoint + 1
            if low < eventCount:
                currentEventValue += maxValueAfterEvent[low]
            highestValue = max(highestValue, currentEventValue)
        return highestValue
