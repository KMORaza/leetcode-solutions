class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for person in people:
            height, k = person
            result.insert(k, person)
        return result