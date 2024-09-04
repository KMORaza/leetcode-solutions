from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
        return list(anagrams.values())