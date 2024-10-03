class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def time_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        current_minutes = time_to_minutes(current)
        correct_minutes = time_to_minutes(correct)
        difference = correct_minutes - current_minutes
        operations = 0
        for increment in [60, 15, 5, 1]:
            operations += difference // increment
            difference %= increment
        return operations