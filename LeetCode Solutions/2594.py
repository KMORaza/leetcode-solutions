class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_in_time(time_limit):
            total_cars = 0
            for rank in ranks:
                # For each mechanic, calculate max cars they can repair within time_limit
                # time = rank * n^2 => n = sqrt(time_limit / rank)
                max_cars_for_mechanic = int((time_limit // rank) ** 0.5)
                total_cars += max_cars_for_mechanic
                if total_cars >= cars:
                    return True
            return total_cars >= cars

        left, right = 1, min(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2
            if can_repair_in_time(mid):
                right = mid
            else:
                left = mid + 1

        return left