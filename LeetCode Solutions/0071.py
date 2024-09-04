class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []
        for component in components:
            if component == '..':
                if stack:
                    stack.pop()
            elif component and component != '.':
                stack.append(component)
        return '/' + '/'.join(stack)
sol = Solution()
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath("/home//foo/"))
print(sol.simplifyPath("/home/user/Documents/../Pictures"))
print(sol.simplifyPath("/../"))
print(sol.simplifyPath("/.../a/../b/c/../d/./"))
