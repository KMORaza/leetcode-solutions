class Solution:
    def smallestSubsequence(self, s: str) -> str:
        frequency = collections.Counter(s)
        stack = []
        in_stack = set()
        for char in s:
            frequency[char] -= 1
            if char in in_stack:
                continue
            while stack and char < stack[-1] and frequency[stack[-1]] > 0:
                in_stack.remove(stack.pop())
            stack.append(char)
            in_stack.add(char)
        return ''.join(stack)
