class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            height_left = height[left]
            height_right = height[right]
            height_min = min(height_left, height_right)
            area = width * height_min
            max_area = max(max_area, area)
            if height_left < height_right:
                left += 1
            else:
                right -= 1
        return max_area