class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        all_or = set()
        current_or = set()
        for num in arr:
            new_or = {num}
            for val in current_or:
                new_or.add(num | val)
            current_or = new_or
            all_or.update(current_or)
        return len(all_or)
