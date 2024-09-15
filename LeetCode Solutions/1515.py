import numpy as np
class Solution:
    def getMinDistSum(self, points):
        num_points = len(points)
        avg_x = sum(point[0] for point in points) / num_points
        avg_y = sum(point[1] for point in points) / num_points
        decay = 0.999
        threshold = 1e-6
        rate = 0.5
        while True:
            grad_x = 0
            grad_y = 0
            total_length = 0
            for point in points:
                diff_x = avg_x - point[0]
                diff_y = avg_y - point[1]
                dist = np.sqrt(diff_x ** 2 + diff_y ** 2)
                dist = dist + 1e-8
                grad_x += diff_x / dist
                grad_y += diff_y / dist
                total_length += dist
            step_x = grad_x * rate
            step_y = grad_y * rate
            if np.sqrt(step_x ** 2 + step_y ** 2) <= threshold:
                return total_length
            avg_x -= step_x
            avg_y -= step_y
            rate *= decay
