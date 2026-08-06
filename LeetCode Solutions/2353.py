from sortedcontainers import SortedList


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_foods = {}

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating

            if cuisine not in self.cuisine_to_foods:
                self.cuisine_to_foods[cuisine] = SortedList()
            self.cuisine_to_foods[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        old_rating = self.food_to_rating[food]

        self.cuisine_to_foods[cuisine].remove((-old_rating, food))
        self.cuisine_to_foods[cuisine].add((-newRating, food))

        self.food_to_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_to_foods[cuisine][0][1]