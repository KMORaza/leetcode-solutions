class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        n = len(s)
        first_group_length = n % k or k
        result = []
        if first_group_length > 0:
            result.append(s[:first_group_length])
        for i in range(first_group_length, n, k):
            result.append(s[i:i + k])
        return '-'.join(result)
