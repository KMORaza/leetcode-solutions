class Solution:
    def findLexSmallestString(self, initial_str: str, increment: int, rotate_by: int) -> str:
        self.smallest_str = initial_str
        self.perform_dfs(initial_str, increment, rotate_by, set())
        return self.smallest_str
    def perform_dfs(self, current_str: str, increment: int, rotate_by: int, visited: set) -> None:
        if current_str in visited:
            return
        visited.add(current_str)
        if self.smallest_str > current_str:
            self.smallest_str = current_str
        self.perform_dfs(self.increment_string(current_str, increment), increment, rotate_by, visited)
        self.perform_dfs(self.rotate_string(current_str, rotate_by), increment, rotate_by, visited)
    def increment_string(self, current_str: str, increment: int) -> str:
        str_list = list(current_str)
        for index in range(1, len(str_list), 2):
            str_list[index] = str((int(current_str[index]) + increment) % 10)
        return ''.join(str_list)
    def rotate_string(self, current_str: str, rotate_by: int) -> str:
        length = len(current_str)
        return current_str[-rotate_by:] + current_str[:-rotate_by]
