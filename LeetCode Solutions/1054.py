from typing import List
from collections import Counter
from heapq import heappush, heappop
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        max_heap = []
        for barcode, freq in count.items():
            heappush(max_heap, (-freq, barcode))
        result = []
        prev_freq, prev_barcode = 0, 0
        while max_heap:
            freq, barcode = heappop(max_heap)
            result.append(barcode)
            if prev_freq < 0:
                heappush(max_heap, (prev_freq, prev_barcode))
            prev_freq = freq + 1
            prev_barcode = barcode
        return result
