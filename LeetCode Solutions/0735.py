from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                top = stack[-1]
                if top < -asteroid:
                    stack.pop()
                elif top == -asteroid:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        return stack
