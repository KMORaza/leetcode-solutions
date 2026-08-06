class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        pos_set = set(positive_feedback)
        neg_set = set(negative_feedback)

        scores = []

        for i in range(len(report)):
            score = 0
            words = report[i].split()
            for word in words:
                if word in pos_set:
                    score += 3
                elif word in neg_set:
                    score -= 1
            scores.append((score, student_id[i]))

        scores.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for i in range(k):
            result.append(scores[i][1])

        return result