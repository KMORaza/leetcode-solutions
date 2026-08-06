class Solution:
    def countTime(self, time: str) -> int:
        hour_part, minute_part = time.split(':')

        hour_options = 1
        if hour_part == '??':
            hour_options = 24
        elif hour_part[0] == '?':
            if hour_part[1] <= '3':
                hour_options = 3
            else:
                hour_options = 2
        elif hour_part[1] == '?':
            if hour_part[0] == '2':
                hour_options = 4
            elif hour_part[0] in '01':
                hour_options = 10
            else:
                hour_options = 1

        minute_options = 1
        if minute_part == '??':
            minute_options = 60
        elif minute_part[0] == '?':
            minute_options = 6
        elif minute_part[1] == '?':
            minute_options = 10

        return hour_options * minute_options