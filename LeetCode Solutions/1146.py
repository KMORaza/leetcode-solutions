class SnapshotArray:
    def __init__(self, size: int):
        self.history = [[] for _ in range(size)]
        for i in range(size):
            self.history[i].append((0, 0))
        self.current_version = 0
    def set(self, position: int, value: int) -> None:
        record_list = self.history[position]
        if record_list[-1][0] == self.current_version:
            record_list[-1] = (self.current_version, value)
        else:
            record_list.append((self.current_version, value))
    def snap(self) -> int:
        last_version = self.current_version
        self.current_version += 1
        return last_version
    def get(self, position: int, version: int) -> int:
        record_list = self.history[position]
        start, end = 0, len(record_list) - 1
        while start <= end:
            mid = (start + end) // 2
            if record_list[mid][0] <= version:
                start = mid + 1
            else:
                end = mid - 1
        if end >= 0 and record_list[end][0] <= version:
            return record_list[end][1]
        return 0
