class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required_codes = 1 << k
        seen_codes = set()
        for i in range(len(s) - k + 1):
            code = s[i:i + k]
            seen_codes.add(code)
            if len(seen_codes) == required_codes:
                return True
        return len(seen_codes) == required_codes
