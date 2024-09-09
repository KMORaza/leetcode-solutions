class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        operations = []
        for i in range(len(indices)):
            index = indices[i]
            source = sources[i]
            target = targets[i]
            if s[index:index + len(source)] == source:
                operations.append((index, source, target))
        operations.sort(reverse=True, key=lambda x: x[0])
        s_list = list(s)
        for index, source, target in operations:
            s_list[index:index + len(source)] = list(target)
        return ''.join(s_list)

