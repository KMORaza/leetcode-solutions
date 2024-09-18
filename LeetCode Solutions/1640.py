from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index_map = {piece[0]: piece for piece in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in index_map:
                return False
            piece = index_map[arr[i]]
            if arr[i:i + len(piece)] != piece:
                return False
            i += len(piece)
        return True
