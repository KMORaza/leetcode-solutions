class Solution:
    def minimumBuckets(self, layout: str) -> int:
        street_array = list(layout)
        for position in range(len(street_array)):
            if street_array[position] == 'H':
                if position > 0 and street_array[position - 1] == 'B':
                    continue
                if position + 1 < len(street_array) and street_array[position + 1] == '.':
                    street_array[position + 1] = 'B'
                elif position > 0 and street_array[position - 1] == '.':
                    street_array[position - 1] = 'B'
                else:
                    return -1
        return street_array.count('B')
