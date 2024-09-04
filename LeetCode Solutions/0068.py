class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        def justify_line(line_words, line_length, is_last_line=False):
            if is_last_line or len(line_words) == 1:
                return ' '.join(line_words).ljust(maxWidth)
            total_spaces = maxWidth - line_length
            num_slots = len(line_words) - 1
            even_space = total_spaces // num_slots
            extra_space = total_spaces % num_slots
            line = ''
            for i in range(num_slots):
                line += line_words[i]
                line += ' ' * (even_space + (1 if i < extra_space else 0))
            line += line_words[-1]
            return line
        result = []
        current_words = []
        current_length = 0
        for word in words:
            if current_length + len(word) + len(current_words) > maxWidth:
                result.append(justify_line(current_words, current_length))
                current_words = []
                current_length = 0
            current_words.append(word)
            current_length += len(word)
        result.append(justify_line(current_words, current_length, is_last_line=True))
        return result
