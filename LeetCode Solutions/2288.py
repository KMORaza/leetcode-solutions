class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        discounted_words = []
        for word in words:
            if word.startswith('$') and word[1:].isdigit():
                price = int(word[1:])
                discounted_price = price * (100 - discount) / 100
                discounted_word = f"${discounted_price:.2f}"
                discounted_words.append(discounted_word)
            else:
                discounted_words.append(word)
        return ' '.join(discounted_words)
