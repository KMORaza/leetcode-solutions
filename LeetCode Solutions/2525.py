class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height

        is_bulky = length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or volume >= 10 ** 9
        is_heavy = mass >= 100

        if is_bulky and is_heavy:
            return "Both"
        elif is_bulky:
            return "Bulky"
        elif is_heavy:
            return "Heavy"
        else:
            return "Neither"