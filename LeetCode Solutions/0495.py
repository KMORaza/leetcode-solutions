class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total_poisoned_time = 0
        last_end_time = 0
        for attack_time in timeSeries:
            start = attack_time
            end = start + duration
            if start > last_end_time:
                total_poisoned_time += duration
            else:
                total_poisoned_time += end - last_end_time
            last_end_time = end
        return total_poisoned_time
