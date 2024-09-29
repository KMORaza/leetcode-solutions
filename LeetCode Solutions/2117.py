class Solution:
    def abbreviateProduct(self, lower_bound: int, upper_bound: int) -> str:
        cumulative_product = 1.0
        trailing_product = 1
        total_digits = 0
        trailing_zeros = 0
        for current_number in range(lower_bound, upper_bound + 1):
            cumulative_product *= current_number
            while cumulative_product >= 1.0:
                cumulative_product /= 10
                total_digits += 1
            trailing_product *= current_number
            while trailing_product % 10 == 0:
                trailing_product //= 10
                trailing_zeros += 1
            if trailing_product > 10**11:
                trailing_product %= 10**11
        if total_digits - trailing_zeros <= 10:
            power_of_ten = 10 ** (total_digits - trailing_zeros)
            return str(int(cumulative_product * power_of_ten + 0.5)) + 'e' + str(trailing_zeros)
        significant_digits = str(int(cumulative_product * 10 ** 5))
        last_five_digits = str(trailing_product)[-5:]
        return significant_digits + '...' + last_five_digits + 'e' + str(trailing_zeros)