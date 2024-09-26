class Solution:
    def numberOfWeakCharacters(self, attributes):
        attributes.sort(key=lambda item: (-item[0], item[1]))
        weak_char_count = 0
        strongest_resilience = 0
        for hero in attributes:
            if hero[1] < strongest_resilience:
                weak_char_count += 1
            strongest_resilience = max(strongest_resilience, hero[1])
        return weak_char_count
