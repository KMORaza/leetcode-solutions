class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev_number = -1
        for word in s.split():
            if word.isdigit():
                current_number = int(word)
                if current_number <= prev_number:
                    return False
                prev_number = current_number
        return True