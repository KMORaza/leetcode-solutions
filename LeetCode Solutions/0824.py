class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        goat_latin_words = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                goat_word = word + 'ma'
            else:
                goat_word = word[1:] + word[0] + 'ma'
            goat_word += 'a' * (i + 1)
            goat_latin_words.append(goat_word)
        return ' '.join(goat_latin_words)
