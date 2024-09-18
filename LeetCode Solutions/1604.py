from typing import List
from collections import defaultdict
from datetime import datetime, timedelta
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        records = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            records[name].append(datetime.strptime(time, "%H:%M"))
        alerts = set()
        for name, times in records.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= timedelta(hours=1):
                    alerts.add(name)
                    break
        return sorted(alerts)
