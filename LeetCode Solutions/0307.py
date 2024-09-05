class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        self.nums = nums
        for i in range(self.n):
            self._update(i, nums[i])
    def _update(self, index: int, delta: int):
        index += 1
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index
    def _query(self, index: int) -> int:
        index += 1
        sum_ = 0
        while index > 0:
            sum_ += self.bit[index]
            index -= index & -index
        return sum_
    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update(index, delta)
    def sumRange(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)
