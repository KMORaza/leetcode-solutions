class DisjointSet:
    def __init__(self, count):
        self.group = list(range(count))
        self.depth = [0] * count
    def combine_by_depth(self, element_x, element_y):
        root_x = self.locate(element_x)
        root_y = self.locate(element_y)
        if root_x == root_y:
            return
        if self.depth[root_x] < self.depth[root_y]:
            self.group[root_x] = root_y
        elif self.depth[root_x] > self.depth[root_y]:
            self.group[root_y] = root_x
        else:
            self.group[root_x] = root_y
            self.depth[root_y] += 1
    def locate(self, element):
        if self.group[element] != element:
            self.group[element] = self.locate(self.group[element])  # Path compression
        return self.group[element]
class Solution:
    def gcdSort(self, nums):
        highest_value = max(nums)
        least_prime_factors = self.prime_sieve(highest_value + 1)
        disjoint_set = DisjointSet(highest_value + 1)
        for value in nums:
            for prime in self.extract_prime_factors(value, least_prime_factors):
                disjoint_set.combine_by_depth(value, prime)
        sorted_values = sorted(nums)
        for index in range(len(nums)):
            if disjoint_set.locate(nums[index]) != disjoint_set.locate(sorted_values[index]):
                return False
        return True
    def prime_sieve(self, limit):
        least_prime_factors = list(range(limit + 1))
        for candidate in range(2, int(limit**0.5) + 1):
            if least_prime_factors[candidate] == candidate:  # `candidate` is prime
                for multiple in range(candidate * candidate, limit, candidate):
                    if least_prime_factors[multiple] == multiple:
                        least_prime_factors[multiple] = candidate
        return least_prime_factors
    def extract_prime_factors(self, number, least_prime_factors):
        prime_factors_collection = []
        while number > 1:
            prime_divisor = least_prime_factors[number]
            prime_factors_collection.append(prime_divisor)
            while number % prime_divisor == 0:
                number //= prime_divisor
        return prime_factors_collection