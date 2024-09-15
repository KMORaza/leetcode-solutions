class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first_occurrence = {}
        last_occurrence = {}
        n = len(s)
        for i in range(n):
            if s[i] not in first_occurrence:
                first_occurrence[s[i]] = i
            last_occurrence[s[i]] = i
        valid_intervals = []
        for i in range(n):
            if i != first_occurrence[s[i]]:
                continue
            l = first_occurrence[s[i]]
            r = last_occurrence[s[i]]
            for j in range(l, r + 1):
                r = max(r, last_occurrence[s[j]])
            valid = True
            for j in range(l, r + 1):
                if last_occurrence[s[j]] > r:
                    valid = False
                    break
            if valid:
                valid_intervals.append((l, r))
        valid_intervals.sort(key=lambda x: x[1])
        result = []
        current_end = -1
        for start, end in valid_intervals:
            if start > current_end:
                result.append(s[start:end + 1])
                current_end = end
        return result
