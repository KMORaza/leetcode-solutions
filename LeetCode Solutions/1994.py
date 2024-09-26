class Solution:
    def numberOfGoodSubsets(self, input_numbers):
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        total_combinations = 1 << len(prime_list)
        largest_value = max(input_numbers)
        subset_counts = [0] * total_combinations
        occurrences = [0] * (largest_value + 1)
        subset_counts[0] = 1
        for number in input_numbers:
            occurrences[number] += 1
        for number in range(2, largest_value + 1):
            if occurrences[number] == 0:
                continue
            if number % 4 == 0 or number % 9 == 0 or number % 25 == 0:
                continue
            prime_bitmask = self.calculate_prime_bitmask(number, prime_list)
            for current_mask in range(total_combinations):
                if current_mask & prime_bitmask:
                    continue
                updated_mask = current_mask | prime_bitmask
                subset_counts[updated_mask] += subset_counts[current_mask] * occurrences[number]
                subset_counts[updated_mask] %= x
        return (self.exponentiate_mod(2, occurrences[1]) * (sum(subset_counts) - 1) % x) % x
    def calculate_prime_bitmask(self, number, prime_list):
        bitmask = 0
        for idx, prime in enumerate(prime_list):
            if number % prime == 0:
                bitmask |= 1 << idx
        return bitmask
    def exponentiate_mod(self, base_value, exponent_value):
        if exponent_value == 0:
            return 1
        if exponent_value % 2 == 1:
            return base_value * self.exponentiate_mod(base_value, exponent_value - 1) % x
        return self.exponentiate_mod(base_value * base_value % x, exponent_value // 2)
x = 10**9+7
