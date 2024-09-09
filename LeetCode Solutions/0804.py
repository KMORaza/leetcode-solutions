class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        char_to_morse = {chr(i + ord('a')): morse_code[i] for i in range(26)}
        unique_transformations = set()
        for word in words:
            morse_transformation = ''.join(char_to_morse[char] for char in word)
            unique_transformations.add(morse_transformation)
        return len(unique_transformations)
