class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def is_continuation_byte(byte):
            return (byte & 0b11000000) == 0b10000000
        n = len(data)
        i = 0
        while i < n:
            byte = data[i]
            if (byte & 0b10000000) == 0b00000000:
                num_bytes = 1
            elif (byte & 0b11100000) == 0b11000000:
                num_bytes = 2
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes = 3
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes = 4
            else:
                return False
            if i + num_bytes - 1 >= n:
                return False
            for j in range(1, num_bytes):
                if not is_continuation_byte(data[i + j]):
                    return False
            i += num_bytes
        return True
