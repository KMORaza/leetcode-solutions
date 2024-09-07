class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(num: str):
            num = num[:-1]
            plus_index = num.find('+')
            if plus_index != -1:
                real = int(num[:plus_index])
                imag = int(num[plus_index + 1:])
            else:
                minus_index = num.find('-')
                real = int(num[:minus_index])
                imag = int(num[minus_index:])
            return real, imag
        a_real, a_imag = parse_complex(num1)
        b_real, b_imag = parse_complex(num2)
        real_part = a_real * b_real - a_imag * b_imag
        imag_part = a_real * b_imag + a_imag * b_real
        return f"{real_part}+{imag_part}i"
