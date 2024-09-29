class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        capitalized_words = []
        for word in words:
            if len(word) >= 3:
                capitalized_words.append(word.capitalize())
            else:
                capitalized_words.append(word.lower())
        return ' '.join(capitalized_words)
