class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()

        passenger_idx = 0
        for bus_time in buses:
            current_capacity = 0
            while current_capacity < capacity and passenger_idx < len(passengers) and passengers[
                passenger_idx] <= bus_time:
                passenger_idx += 1
                current_capacity += 1

        if current_capacity < capacity:
            candidate = buses[-1]
            if passenger_idx == 0 or passengers[passenger_idx - 1] != candidate:
                return candidate

        latest_passenger = passengers[passenger_idx - 1]
        passenger_set = set(passengers)

        while latest_passenger in passenger_set:
            latest_passenger -= 1

        return latest_passenger