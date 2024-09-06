class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def next_index(index):
            return (index + nums[index]) % len(nums)
        def is_valid_cycle(start_index):
            direction = nums[start_index] > 0
            slow = start_index
            fast = next_index(start_index)
            while nums[fast] * nums[start_index] > 0 and nums[next_index(fast)] * nums[start_index] > 0:
                if slow == fast:
                    if slow == next_index(slow):
                        return False
                    return True
                slow = next_index(slow)
                fast = next_index(next_index(fast))
            return False
        for i in range(len(nums)):
            if nums[i] != 0:
                if is_valid_cycle(i):
                    return True
        return False
