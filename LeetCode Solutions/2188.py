class Solution:
    def minimumFinishTime(self, tireSpecifications, pitStopDuration, totalCircuits):
        tireCost = [float('inf')] * (totalCircuits + 1)
        totalTime = [float('inf')] * (totalCircuits + 1)
        for initialTime, wearFactor in tireSpecifications:
            cumulativeTime = 0
            currentPower = 1
            for laps in range(1, totalCircuits + 1):
                if initialTime * currentPower >= pitStopDuration + initialTime:
                    break
                cumulativeTime += initialTime * currentPower
                tireCost[laps] = min(tireCost[laps], cumulativeTime)
                currentPower *= wearFactor
        totalTime[0] = 0
        for laps in range(1, totalCircuits + 1):
            for j in range(1, laps + 1):
                totalTime[laps] = min(totalTime[laps], totalTime[laps - j] + pitStopDuration + tireCost[j])
        return totalTime[totalCircuits] - pitStopDuration