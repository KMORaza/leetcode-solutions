class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]
    def addCar(self, carType: int) -> bool:
        if self.spaces[carType - 1] > 0:
            self.spaces[carType - 1] -= 1
            return True
        return False