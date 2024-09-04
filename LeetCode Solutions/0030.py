from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        if len(s) < total_len:
            return []
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        result = []
        for i in range(word_len):
            left = i
            right = i
            window_count = defaultdict(int)
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                if word in word_count:
                    window_count[word] += 1
                    while window_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        left += word_len
                    if right - left == total_len:
                        result.append(left)
                else:
                    window_count.clear()
                    left = right
        return result