from bisect import bisect_left
class Record:
    def __init__(self, title: str, score_value: int):
        self.title = title
        self.score_value = score_value
    def __lt__(self, other):
        if self.score_value == other.score_value:
            return self.title < other.title
        return self.score_value > other.score_value
class SORTracker:
    def __init__(self):
        self.data_collection = []
        self.position = 0
    def add(self, title: str, score_value: int):
        self.insert_in_order(Record(title, score_value))
    def get(self) -> str:
        current_record = self.data_collection[self.position]
        self.position += 1
        return current_record.title
    def insert_in_order(self, record: Record):
        index = bisect_left(self.data_collection, record)
        self.data_collection.insert(index, record)

