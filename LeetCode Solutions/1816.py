class Solution:
    def truncateSentence(self, sentence: str, wordCount: int) -> str:
        words = sentence.split()
        truncated = words[:wordCount]
        return ' '.join(truncated)
