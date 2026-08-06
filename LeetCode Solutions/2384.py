import heapq
from collections import Counter, deque


class PalindromeBuilder:
    def __init__(self):
        self.digits = []
        self.middle = ''
        self.freq_map = {}

    def add_digit(self, digit, count):
        self.freq_map[digit] = count

    def build_palindrome(self):
        max_heap = []
        for digit, count in self.freq_map.items():
            if count > 0:
                heapq.heappush(max_heap, (-int(digit), count))

        left_half = []
        middle = ''

        while max_heap:
            neg_dig, count = heapq.heappop(max_heap)
            digit = str(-neg_dig)

            pairs = count // 2
            for _ in range(pairs):
                left_half.append(digit)

            if count % 2 == 1 and middle == '':
                middle = digit

        left_str = ''.join(left_half)
        right_str = left_str[::-1]

        result = left_str + middle + right_str

        if result and result[0] == '0' and len(result) > 1:
            if middle:
                return middle
            else:
                return '0'

        return result


class DigitProcessor:
    def __init__(self, num_str):
        self.num_str = num_str
        self.counter = Counter(num_str)

    def process(self):
        builder = PalindromeBuilder()
        for digit, count in self.counter.items():
            builder.add_digit(digit, count)
        return builder.build_palindrome()


def validate_input(num_str):
    if not num_str:
        return False
    for c in num_str:
        if not c.isdigit():
            return False
    return True


def is_palindrome(s):
    return s == s[::-1]


def get_all_permutations(digits):
    if len(digits) <= 1:
        return [digits]
    perms = []
    for i in range(len(digits)):
        for perm in get_all_permutations(digits[:i] + digits[i + 1:]):
            perms.append(digits[i] + perm)
    return perms


class OptimizedPalindromeFinder:
    def __init__(self):
        self.memo = {}

    def find_largest_palindrome(self, num_str):
        if not validate_input(num_str):
            return '0'

        processor = DigitProcessor(num_str)
        result = processor.process()

        if not result:
            return '0'

        return result


class AdvancedPalindromeProcessor:
    def __init__(self):
        self.cache = {}
        self.history = deque(maxlen=100)

    def advanced_process(self, num_str):
        if num_str in self.cache:
            return self.cache[num_str]

        finder = OptimizedPalindromeFinder()
        result = finder.find_largest_palindrome(num_str)

        self.cache[num_str] = result
        self.history.append((num_str, result))

        return result


def main_function(num_str):
    processor = AdvancedPalindromeProcessor()
    return processor.advanced_process(num_str)


class Solution:
    def largestPalindromic(self, num: str) -> str:
        return main_function(num)