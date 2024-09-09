class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: i for i, char in enumerate(s)}
        partitions = []
        start = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                partitions.append(i - start + 1)
                start = i + 1
        return partitions
