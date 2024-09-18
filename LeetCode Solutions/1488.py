from sortedcontainers import SortedSet
class Solution:
    def avoidFlood(self, precipitation):
        total_days = len(precipitation)
        outcome = [-1] * total_days
        clear_days = SortedSet()
        last_rain_event = {}
        for current_day in range(total_days):
            current_lake = precipitation[current_day]
            if current_lake > 0:
                if current_lake in last_rain_event:
                    next_available_day_index = clear_days.bisect_right(last_rain_event[current_lake])
                    if next_available_day_index == len(clear_days):
                        return []
                    next_available_day = clear_days[next_available_day_index]
                    outcome[next_available_day] = current_lake
                    clear_days.remove(next_available_day)
                last_rain_event[current_lake] = current_day
            else:
                clear_days.add(current_day)
                outcome[current_day] = 1
        return outcome
