from collections import defaultdict
from sortedcontainers import SortedSet
from typing import List, Tuple
class MovieRentingSystem:
    class RentalRecord:
        def __init__(self, fee: int, vendor: int, title: int):
            self.fee = fee
            self.vendor = vendor
            self.title = title
        def __lt__(self, other):
            if self.fee != other.fee:
                return self.fee < other.fee
            if self.vendor != other.vendor:
                return self.vendor < other.vendor
            return self.title < other.title
        def __eq__(self, other):
            return (self.fee, self.vendor, self.title) == (other.fee, other.vendor, other.title)
        def __hash__(self):
            return hash((self.fee, self.vendor, self.title))
    def __init__(self, num_vendors: int, rental_entries: List[Tuple[int, int, int]]):
        self.available_records = defaultdict(SortedSet)
        self.vendor_title_fee_map = {}
        self.active_rentals = SortedSet()
        for vendor, title, fee in rental_entries:
            record = self.RentalRecord(fee, vendor, title)
            self.available_records[title].add(record)
            self.vendor_title_fee_map[(vendor, title)] = fee
    def search(self, title: int) -> List[int]:
        return [record.vendor for record in self.available_records.get(title, SortedSet())[:5]]
    def rent(self, vendor: int, title: int):
        fee = self.vendor_title_fee_map[(vendor, title)]
        record = self.RentalRecord(fee, vendor, title)
        self.available_records[title].remove(record)
        self.active_rentals.add(record)
    def drop(self, vendor: int, title: int):
        fee = self.vendor_title_fee_map[(vendor, title)]
        record = self.RentalRecord(fee, vendor, title)
        self.available_records[title].add(record)
        self.active_rentals.remove(record)
    def report(self) -> List[List[int]]:
        return [[record.vendor, record.title] for record in self.active_rentals[:5]]
