from typing import List
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        for path in folder:
            if not result or not path.startswith(result[-1] + '/'):
                result.append(path)
        return result
