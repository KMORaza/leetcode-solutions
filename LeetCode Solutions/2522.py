class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        i = 0
        partitions = 0

        while i < n:
            num = 0
            j = i

            while j < n:
                digit = int(s[j])
                new_num = num * 10 + digit

                if new_num > k:
                    break

                num = new_num
                j += 1

            if j == i:
                return -1

            partitions += 1
            i = j

        return partitions