class Solution:
    def numFriendRequests(self, ages):
        output = 0
        count = [0] * 121
        for age in ages:
            count[age] += 1
        for ageA in range(1, 121):
            for ageB in range(1, 121):
                countA = count[ageA]
                countB = count[ageB]
                if countA > 0 and countB > 0 and self.request(ageA, ageB):
                    if ageA == ageB:
                        output += countA * (countB - 1)
                    else:
                        output += countA * countB
        return output
    def request(self, ageA, ageB):
        return not (ageB <= 0.5 * ageA + 7 or ageB > ageA or (ageB > 100 and ageA < 100))
