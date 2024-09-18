class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities = set()
        for start, end in paths:
            start_cities.add(start)
        for _, end in paths:
            if end not in start_cities:
                return end
