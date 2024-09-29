class Solution:
    def kthSmallestProduct(self, first_array, second_array, k: int) -> int:
        negative_first, positive_first = [], []
        negative_second, positive_second = [], []
        self.partition(first_array, negative_first, positive_first)
        self.partition(second_array, negative_second, positive_second)
        total_negative_count = len(negative_first) * len(positive_second) + len(positive_first) * len(negative_second)
        result_sign = 1
        if k > total_negative_count:
            k -= total_negative_count
        else:
            k = total_negative_count - k + 1
            result_sign = -1
            negative_second, positive_second = positive_second, negative_second
        lower_bound, upper_bound = 0, 10**10
        while lower_bound < upper_bound:
            midpoint = (lower_bound + upper_bound) // 2
            if self.countProductsNotExceeding(negative_first, positive_second, midpoint) + self.countProductsNotExceeding(positive_first, negative_second, midpoint) >= k:
                upper_bound = midpoint
            else:
                lower_bound = midpoint + 1
        return result_sign * lower_bound
    def partition(self, array, neg_collection, pos_collection):
        for value in array:
            if value < 0:
                neg_collection.append(-value)
            else:
                pos_collection.append(value)
        neg_collection.reverse()
    def countProductsNotExceeding(self, neg_collection, pos_collection, threshold):
        product_count = 0
        index = len(pos_collection) - 1
        for a in neg_collection:
            while index >= 0 and a * pos_collection[index] > threshold:
                index -= 1
            product_count += index + 1
        return product_count
