from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            identifier, content = log.split(' ', 1)
            if content[0].isalpha():
                letter_logs.append((content, identifier))
            else:
                digit_logs.append(log)
        letter_logs.sort(key=lambda x: (x[0], x[1]))
        result = [f"{identifier} {content}" for content, identifier in letter_logs] + digit_logs
        return result
