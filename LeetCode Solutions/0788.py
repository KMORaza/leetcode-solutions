class Solution:
    def rotatedDigits(self, n: int) -> int:
        def rotate_digit(digit):
            rotation_map = {
                '0': '0',
                '1': '1',
                '2': '5',
                '5': '2',
                '6': '9',
                '8': '8',
                '9': '6'
            }
            return rotation_map.get(digit, None)
        def is_good_number(number):
            str_number = str(number)
            rotated_str_parts = [rotate_digit(d) for d in str_number]
            if None in rotated_str_parts:
                return False
            rotated_str = ''.join(rotated_str_parts)
            return rotated_str != str_number
        count = 0
        for i in range(1, n + 1):
            if is_good_number(i):
                count += 1
        return count
