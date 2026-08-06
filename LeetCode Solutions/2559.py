class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        prefix = [0]

        for word in words:
            is_vowel_string = 1 if word[0] in vowels and word[-1] in vowels else 0
            prefix.append(prefix[-1] + is_vowel_string)

        result = []
        for l, r in queries:
            result.append(prefix[r + 1] - prefix[l])

        return result