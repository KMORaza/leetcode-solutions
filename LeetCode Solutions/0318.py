class Solution:
    def maxProduct(self, words):
        def get_bitmask(word):
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
            return bitmask
        n = len(words)
        bitmasks = [get_bitmask(word) for word in words]
        lengths = [len(word) for word in words]
        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:
                    product = lengths[i] * lengths[j]
                    if product > max_product:
                        max_product = product
        return max_product
