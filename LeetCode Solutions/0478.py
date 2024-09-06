import random
import math
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
    def randPoint(self) -> list:
        r = math.sqrt(random.uniform(0, self.radius ** 2))
        theta = random.uniform(0, 2 * math.pi)
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]
