class Solution:
    def countVowelSubstrings(self, input_string: str) -> int:
        return self.computeVowelSubstringsWithLimit(input_string, 5) - self.computeVowelSubstringsWithLimit(input_string, 4)
    def computeVowelSubstringsWithLimit(self, str_data: str, max_unique: int) -> int:
        substring_count = 0
        unique_vowel_count = max_unique
        vowel_frequency = [0] * 26
        start_index = 0
        for end_index in range(len(str_data)):
            if not self.isCharacterVowel(str_data[end_index]):
                start_index = end_index + 1
                unique_vowel_count = max_unique
                vowel_frequency = [0] * 26
                continue
            if vowel_frequency[ord(str_data[end_index]) - ord('a')] == 0:
                unique_vowel_count -= 1
            vowel_frequency[ord(str_data[end_index]) - ord('a')] += 1
            while unique_vowel_count < 0:
                vowel_frequency[ord(str_data[start_index]) - ord('a')] -= 1
                if vowel_frequency[ord(str_data[start_index]) - ord('a')] == 0:
                    unique_vowel_count += 1
                start_index += 1
            substring_count += end_index - start_index + 1
        return substring_count
    def isCharacterVowel(self, character: str) -> bool:
        return character in "aeiou"
