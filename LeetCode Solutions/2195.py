class Solution:
    def minimalKSum(self, number_list: list[int], desired_count: int) -> int:
        cumulative_sum = 0
        number_list.sort()
        if number_list[0] > 1:
            start = 1
            end = min(desired_count, number_list[0] - 1)
            cumulative_sum += (start + end) * (end - start + 1) // 2
            desired_count -= (end - start + 1)
            if desired_count == 0:
                return cumulative_sum
        for idx in range(len(number_list) - 1):
            if number_list[idx] == number_list[idx + 1]:
                continue
            start = number_list[idx] + 1
            end = min(number_list[idx] + desired_count, number_list[idx + 1] - 1)
            cumulative_sum += (start + end) * (end - start + 1) // 2
            desired_count -= (end - start + 1)
            if desired_count == 0:
                return cumulative_sum
        if desired_count > 0:
            start = number_list[-1] + 1
            end = number_list[-1] + desired_count
            cumulative_sum += (start + end) * (end - start + 1) // 2
        return cumulative_sum