class Solution:
    def maskPII(self, input: str) -> str:
        if input[0].isalpha():
            input = input.lower()
            at_index = input.index('@')
            return f"{input[0]}*****{input[at_index-1:]}"
        digit_maker = []
        for c in input:
            if c.isdigit():
                digit_maker.append(c)
        digits = ''.join(digit_maker)
        international_code_length = len(digits) - 10
        masked_suffix = f"***-***-{digits[-4:]}"
        if international_code_length == 0:
            return masked_suffix
        else:
            stars_for_international = "+" + "*" * international_code_length
            return f"{stars_for_international}-{masked_suffix}"
