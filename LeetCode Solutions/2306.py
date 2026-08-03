class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        suffix_groups = {}
        for idea in ideas:
            first_char = idea[0]
            suffix = idea[1:]
            if first_char not in suffix_groups:
                suffix_groups[first_char] = set()
            suffix_groups[first_char].add(suffix)
        
        result = 0
        chars = list(suffix_groups.keys())
        for i in range(len(chars)):
            for j in range(i + 1, len(chars)):
                char1, char2 = chars[i], chars[j]
                group1, group2 = suffix_groups[char1], suffix_groups[char2]
                
                common_suffixes = group1 & group2
                unique1 = len(group1) - len(common_suffixes)
                unique2 = len(group2) - len(common_suffixes)
                
                result += unique1 * unique2 * 2
        
        return result
