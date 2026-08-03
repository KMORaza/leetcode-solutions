class Solution:
    def greatestLetter(self, s: str) -> str:
        seen_lower = set()
        seen_upper = set()
        
        for c in s:
            if c.islower():
                seen_lower.add(c)
            else:
                seen_upper.add(c.lower())
        
        common = seen_lower & seen_upper
        if not common:
            return ""
        
        greatest = max(common)
        return greatest.upper()
