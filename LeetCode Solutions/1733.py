class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cannot_communicate = set()
        for f in friendships:
            if not set(languages[f[0] - 1]).intersection(set(languages[f[1] - 1])):
                cannot_communicate.add(f[0])
                cannot_communicate.add(f[1])
        if not cannot_communicate:
            return 0
        language_count = [0] * (n + 1)
        for person in cannot_communicate:
            for lang in languages[person - 1]:
                language_count[lang] += 1
        return len(cannot_communicate) - max(language_count)
