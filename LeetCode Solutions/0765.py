class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        index_map = {person: i for i, person in enumerate(row)}
        swaps = 0
        for i in range(0, len(row), 2):
            person1 = row[i]
            person2 = person1 ^ 1
            if row[i + 1] != person2:
                partner_index = index_map[person2]
                row[partner_index], row[i + 1] = row[i + 1], row[partner_index]
                index_map[row[partner_index]] = partner_index
                index_map[row[i + 1]] = i + 1
                swaps += 1
        return swaps
