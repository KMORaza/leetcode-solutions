class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total_skill = skill[0] + skill[-1]
        chemistry = 0

        for i in range(n // 2):
            left = i
            right = n - 1 - i
            if skill[left] + skill[right] != total_skill:
                return -1
            chemistry += skill[left] * skill[right]

        return chemistry