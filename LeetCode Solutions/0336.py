class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]
        word_map = {word: i for i, word in enumerate(words)}
        result = []
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                left = word[:j]
                right = word[j:]
                if is_palindrome(left):
                    reversed_right = right[::-1]
                    if reversed_right != word and reversed_right in word_map:
                        result.append([word_map[reversed_right], i])
                if j != n and is_palindrome(right):
                    reversed_left = left[::-1]
                    if reversed_left != word and reversed_left in word_map:
                        result.append([i, word_map[reversed_left]])
        return result
