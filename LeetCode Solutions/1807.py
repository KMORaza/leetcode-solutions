from typing import List
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = {key: value for key, value in knowledge}
        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                end = s.find(')', i)
                if end == -1:
                    result.append(s[i])
                    break
                variable = s[i + 1:end]
                result.append(knowledge_dict.get(variable, '?'))
                i = end + 1
            else:
                result.append(s[i])
                i += 1
        return ''.join(result)
