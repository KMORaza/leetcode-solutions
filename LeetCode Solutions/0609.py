from typing import List
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_name, file_content = file_info.split('(')
                file_content = file_content.rstrip(')')
                file_path = f"{directory}/{file_name}"
                content_to_paths[file_content].append(file_path)
        result = [paths for paths in content_to_paths.values() if len(paths) > 1]
        return result
