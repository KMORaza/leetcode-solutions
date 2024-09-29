from typing import List
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_set = set()
        for word in startWords:
            start_set.add(''.join(sorted(word)))
        count = 0
        for target in targetWords:
            for i in range(len(target)):
                modified_word = target[:i] + target[i+1:]
                if ''.join(sorted(modified_word)) in start_set:
                    count += 1
                    break
        return count