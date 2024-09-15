class Solution:
    def distinctEchoSubstrings(self, s: str) -> int:
        def generate_substrings(s: str):
            n = len(s)
            substrings = set()
            for length in range(1, n // 2 + 1):
                for start in range(n - 2 * length + 1):
                    substr = s[start:start + length]
                    echo_substr = s[start:start + 2 * length]
                    if echo_substr == substr + substr:
                        substrings.add(echo_substr)
            return substrings
        substrings = generate_substrings(s)
        return len(substrings)
