class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def date_to_day(date_str):
            month, day = map(int, date_str.split('-'))
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            day_of_year = 0
            for i in range(month - 1):
                day_of_year += days_in_month[i]
            day_of_year += day
            return day_of_year

        alice_start = date_to_day(arriveAlice)
        alice_end = date_to_day(leaveAlice)
        bob_start = date_to_day(arriveBob)
        bob_end = date_to_day(leaveBob)

        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)

        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        else:
            return 0