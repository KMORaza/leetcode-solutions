class Solution:
    def restoreIpAddresses(self, s: str):
        def is_valid(segment):
            return len(segment) <= 3 and (segment[0] != '0' or segment == "0") and int(segment) <= 255
        def backtrack(start=0, path=[]):
            if len(path) == 4 and start == len(s):
                result.append(".".join(path))
                return
            if len(path) == 4:
                return
            for end in range(start, min(start + 3, len(s))):
                segment = s[start:end + 1]
                if is_valid(segment):
                    backtrack(end + 1, path + [segment])
        result = []
        backtrack()
        return result
