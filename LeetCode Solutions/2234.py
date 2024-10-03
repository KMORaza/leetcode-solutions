class Solution:
    def maximumBeauty(self, flower_array, extra_flowers, desired_bloom, full_bloom_score, partial_bloom_score):
        flower_array.sort()
        total_flower_count = len(flower_array)
        sum_prefix = [0] * (total_flower_count + 1)
        for index in range(total_flower_count):
            sum_prefix[index + 1] = sum_prefix[index] + flower_array[index]
        max_bloom_value = 0
        fully_bloomed_count = 0
        for flower in flower_array:
            if flower >= desired_bloom:
                fully_bloomed_count += 1
        while fully_bloomed_count <= total_flower_count:
            extra_flowers -= (0 if fully_bloomed_count == 0 else max(desired_bloom - flower_array[total_flower_count - fully_bloomed_count], 0))
            if extra_flowers < 0:
                break
            low, high = 0, total_flower_count - fully_bloomed_count - 1
            while low < high:
                mid = (low + high + 1) // 2
                if flower_array[mid] * (mid + 1) - sum_prefix[mid + 1] <= extra_flowers:
                    low = mid
                else:
                    high = mid - 1
            partial_bloom_max = 0
            if high != -1:
                cost_to_full = flower_array[low] * (low + 1) - sum_prefix[low + 1]
                partial_bloom_max = min(flower_array[low] + (extra_flowers - cost_to_full) // (low + 1), desired_bloom - 1)
            max_bloom_value = max(max_bloom_value, fully_bloomed_count * full_bloom_score + partial_bloom_max * partial_bloom_score)
            fully_bloomed_count += 1
        return max_bloom_value
