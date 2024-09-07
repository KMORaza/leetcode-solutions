class Solution:
    def nearestPalindromic(self, n: str) -> str:
        original_number = int(n)
        closest_palindrome = None
        candidates = self.getCandidates(n, original_number)
        for candidate in candidates:
            if (closest_palindrome is None or
                abs(candidate - original_number) < abs(closest_palindrome - original_number) or
                (abs(candidate - original_number) == abs(closest_palindrome - original_number) and candidate < closest_palindrome)):
                closest_palindrome = candidate
        return str(closest_palindrome)
    def getCandidates(self, n: str, original_number: int) -> set:
        length = len(n)
        candidates = set()
        candidates.add(10**(length - 1) - 1)
        candidates.add(10**length + 1)
        first_half = int(n[:(length + 1) // 2])
        for i in range(first_half - 1, first_half + 2):
            prefix = str(i)
            if length % 2 == 0:
                candidate = prefix + prefix[::-1]
            else:
                candidate = prefix + prefix[-2::-1]
            candidates.add(int(candidate))
        candidates.discard(original_number)
        return candidates
