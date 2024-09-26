class Solution:
    def firstDayBeenInAllRooms(self, roomSequence):
        x = 10**9+7
        totalRooms = len(roomSequence)
        visitDays = [0] * totalRooms
        for currentRoom in range(1, totalRooms):
            visitDays[currentRoom] = (2 * visitDays[currentRoom - 1] - visitDays[roomSequence[currentRoom - 1]] + 2) % x
            if visitDays[currentRoom] < 0:
                visitDays[currentRoom] += x
        return visitDays[totalRooms - 1]