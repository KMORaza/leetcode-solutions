class Solution:
    def minimumDeletions(self, input_string: str) -> int:
        deletions_needed = 0
        count_of_b = 0
        for character in input_string:
            if character == 'a':
                deletions_needed = min(deletions_needed + 1, count_of_b)
            else:
                count_of_b += 1
        return deletions_needed
