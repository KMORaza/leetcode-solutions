class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tokens = preorder.split(',')
        slots = 1
        for token in tokens:
            if slots == 0:
                return False
            if token == '#':
                slots -= 1
            else:
                slots += 1
        return slots == 0
