class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        max_length = 0
        depth_length = {0: 0}
        for line in lines:
            depth = line.count('\t')
            name = line[depth:]
            if '.' in name:
                current_length = depth_length[depth] + len(name)
                max_length = max(max_length, current_length)
            else:
                depth_length[depth + 1] = depth_length[depth] + len(name) + 1
        return max_length
