class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list:
        def count_bits(x):
            return bin(x).count('1')
        result = []
        for hour in range(12):
            for minute in range(60):
                if count_bits(hour) + count_bits(minute) == turnedOn:
                    time_str = f"{hour}:{minute:02d}"
                    result.append(time_str)
        return result