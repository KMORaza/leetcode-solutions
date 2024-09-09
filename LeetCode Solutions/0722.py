from typing import List
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        commenting = False
        modified = []
        for line in source:
            i = 0
            while i < len(line):
                if i + 1 == len(line):
                    if not commenting:
                        modified.append(line[i])
                    i += 1
                    break
                two_chars = line[i:i+2]
                if two_chars == "/*" and not commenting:
                    commenting = True
                    i += 2
                elif two_chars == "*/" and commenting:
                    commenting = False
                    i += 2
                elif two_chars == "//":
                    if not commenting:
                        break
                    else:
                        i += 2
                else:
                    if not commenting:
                        modified.append(line[i])
                    i += 1
            if modified and not commenting:
                result.append(''.join(modified))
                modified = []
        return result
