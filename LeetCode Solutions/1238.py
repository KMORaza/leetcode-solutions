from typing import List
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def generate_gray_code(n: int) -> List[int]:
            if n == 0:
                return [0]
            prev_gray = generate_gray_code(n - 1)
            reflected = [(1 << (n - 1)) | code for code in reversed(prev_gray)]
            return prev_gray + reflected
        gray_code_sequence = generate_gray_code(n)
        start_index = gray_code_sequence.index(start)
        result = gray_code_sequence[start_index:] + gray_code_sequence[:start_index]
        return result
