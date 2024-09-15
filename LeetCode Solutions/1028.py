class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def create_node(val):
            return TreeNode(int(val))
        stack = []
        i = 0
        n = len(S)
        while i < n:
            level = 0
            while i < n and S[i] == '-':
                level += 1
                i += 1
            val = ''
            while i < n and S[i] != '-':
                val += S[i]
                i += 1
            node = create_node(val)
            while len(stack) > level:
                stack.pop()
            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
        return stack[0]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
