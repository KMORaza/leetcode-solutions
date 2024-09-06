class Solution:
    def construct(self, grid):
        def isUniform(x1, y1, x2, y2):
            initial_value = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] != initial_value:
                        return False
            return True
        def buildTree(x1, y1, x2, y2):
            if isUniform(x1, y1, x2, y2):
                return Node(val=grid[x1][y1] == 1, isLeaf=True)
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
            topLeft = buildTree(x1, y1, mid_x, mid_y)
            topRight = buildTree(x1, mid_y, mid_x, y2)
            bottomLeft = buildTree(mid_x, y1, x2, mid_y)
            bottomRight = buildTree(mid_x, mid_y, x2, y2)
            return Node(val=True, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)
        n = len(grid)
        return buildTree(0, 0, n, n)
