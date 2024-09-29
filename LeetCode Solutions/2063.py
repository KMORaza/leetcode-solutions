class Solution:
    def countVowels(self, word: str) -> int:
        total_vowel_count = 0
        n = len(word)
        for i in range(n):
            if word[i] in 'aeiou':
                total_vowel_count += (i + 1) * (n - i)
        return total_vowel_count
