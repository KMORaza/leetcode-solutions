class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def get_signature(word):
            return frozenset(word)

        signature_count = {}
        for word in words:
            sig = get_signature(word)
            signature_count[sig] = signature_count.get(sig, 0) + 1

        result = 0
        for count in signature_count.values():
            if count > 1:
                result += count * (count - 1) // 2

        return result