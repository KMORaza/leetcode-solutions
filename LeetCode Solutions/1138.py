class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos = {chr(97 + i): (i // 5, i % 5) for i in range(26)}
        x, y = 0, 0
        path = []
        for letter in target:
            tx, ty = pos[letter]
            if tx < x:
                path.append('U' * (x - tx))
            if ty < y:
                path.append('L' * (y - ty))
            if tx > x:
                path.append('D' * (tx - x))
            if ty > y:
                path.append('R' * (ty - y))
            path.append('!')
            x, y = tx, ty
        return ''.join(path)
