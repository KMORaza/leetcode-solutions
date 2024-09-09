from typing import List
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def in_bounds(x: int, y: int) -> bool:
            return 0 <= x < len(image) and 0 <= y < len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and image[nx][ny] == original_color:
                    image[nx][ny] = color
                    queue.append((nx, ny))
        return image

'''
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(x: int, y: int):
            if (x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or 
                image[x][y] != original_color or image[x][y] == color):
                return
            image[x][y] = color
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)        
        original_color = image[sr][sc]
        if original_color != color:
            dfs(sr, sc)
        return image
'''