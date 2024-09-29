class Solution:
    def scoreOfStudents(self, equation: str, responses: list[int]) -> int:
        total_terms = len(equation) // 2 + 1
        cumulative_score = 0
        possible_values = [[set() for _ in range(total_terms)] for _ in range(total_terms)]
        response_count = {}
        for term_index in range(total_terms):
            possible_values[term_index][term_index].add(int(equation[term_index * 2]))
        for gap in range(1, total_terms):
            for start_idx in range(total_terms - gap):
                end_idx = start_idx + gap
                for partition_idx in range(start_idx, end_idx):
                    operator = equation[partition_idx * 2 + 1]
                    for left_value in possible_values[start_idx][partition_idx]:
                        for right_value in possible_values[partition_idx + 1][end_idx]:
                            computed_result = self.calculate(operator, left_value, right_value)
                            if computed_result <= 1000:
                                possible_values[start_idx][end_idx].add(computed_result)
        correct_result = self.compute(equation)
        for response in responses:
            response_count[response] = response_count.get(response, 0) + 1
        for response, count in response_count.items():
            if response == correct_result:
                cumulative_score += 5 * count
            elif response in possible_values[0][total_terms - 1]:
                cumulative_score += 2 * count
        return cumulative_score
    def compute(self, equation: str) -> int:
        result_sum = 0
        current_value = 0
        last_value = 0
        last_operator = '+'
        for index, character in enumerate(equation):
            if character.isdigit():
                current_value = current_value * 10 + int(character)
            if not character.isdigit() or index == len(equation) - 1:
                if last_operator == '+':
                    result_sum += last_value
                    last_value = current_value
                elif last_operator == '*':
                    last_value *= current_value
                last_operator = character
                current_value = 0
        return result_sum + last_value
    def calculate(self, operator: str, left_operand: int, right_operand: int) -> int:
        if operator == '+':
            return left_operand + right_operand
        return left_operand * right_operand
