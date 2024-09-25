class Solution:
    x = 100001
    y = int(10**11 + 7)
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        longest_length = 0
        min_length = min(len(path) for path in paths)
        self.powers = [0] * (min_length + 1)
        self.powers[0] = 1
        for i in range(1, min_length + 1):
            self.powers[i] = (self.powers[i - 1] * self.x) % self.y
        start, end = 1, min_length
        while start <= end:
            mid_length = (start + end) // 2
            if self.hasCommonSubstring(paths, mid_length):
                longest_length = mid_length
                start = mid_length + 1
            else:
                end = mid_length - 1
        return longest_length
    def hasCommonSubstring(self, paths: List[List[int]], length: int) -> bool:
        hash_set = self.computeRollingHash(paths[0], length)
        for path in paths[1:]:
            hash_set.intersection_update(self.computeRollingHash(path, length))
            if not hash_set:
                return False
        return True
    def computeRollingHash(self, array: List[int], length: int) -> set:
        hash_set = set()
        hash_value = 0
        for i in range(length):
            hash_value = (hash_value * self.x + array[i]) % self.y
        hash_set.add(hash_value)
        for current in range(length, len(array)):
            hash_value = (hash_value * self.x % self.y - array[current - length] * self.powers[length] % self.y + array[current]) % self.y
            hash_value = (hash_value + self.y) % self.y
            hash_set.add(hash_value)
        return hash_set