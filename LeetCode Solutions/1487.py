from typing import List
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_count = {}
        result = []
        for name in names:
            original_name = name
            if name not in name_count:
                result.append(name)
                name_count[name] = 1
            else:
                k = name_count[name]
                while f"{name}({k})" in name_count:
                    k += 1
                new_name = f"{name}({k})"
                result.append(new_name)
                name_count[new_name] = 1
                name_count[name] = k + 1
        return result
