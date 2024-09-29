class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = {}
        palindrome_length = 0
        has_center = False
        for word in words:
            count[word] = count.get(word, 0) + 1
        for word, freq in count.items():
            if word[0] == word[1]:
                palindrome_length += (freq // 2) * 4
                if freq % 2 == 1:
                    has_center = True
            else:
                reverse_word = word[::-1]
                if reverse_word in count:
                    palindrome_length += min(freq, count[reverse_word]) * 4
                    count[reverse_word] = 0
        return palindrome_length + 2 if has_center else palindrome_length