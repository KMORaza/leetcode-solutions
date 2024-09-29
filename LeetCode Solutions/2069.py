class Robot:
    def __init__(self, width: int, height: int):
        self.origin_status = True
        self.current_index = 0
        self.coordinates = []
        self.coordinates.append(([0, 0], "South"))
        for x in range(1, width):
            self.coordinates.append(([x, 0], "East"))
        for y in range(1, height):
            self.coordinates.append(([width - 1, y], "North"))
        for x in range(width - 2, -1, -1):
            self.coordinates.append(([x, height - 1], "West"))
        for y in range(height - 2, 0, -1):
            self.coordinates.append(([0, y], "South"))
    def step(self, num: int):
        self.origin_status = False
        self.current_index = (self.current_index + num) % len(self.coordinates)
    def getPos(self) -> list:
        return self.coordinates[self.current_index][0]
    def getDir(self) -> str:
        return "East" if self.origin_status else self.coordinates[self.current_index][1]

