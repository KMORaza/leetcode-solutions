class UndergroundSystem:
    def __init__(self):
        self.check_in_times = {}
        self.travel_times = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_times[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_in_times.pop(id)
        travel_time = t - check_in_time
        if (start_station, stationName) not in self.travel_times:
            self.travel_times[(start_station, stationName)] = [0, 0]
        self.travel_times[(start_station, stationName)][0] += travel_time
        self.travel_times[(start_station, stationName)][1] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count
