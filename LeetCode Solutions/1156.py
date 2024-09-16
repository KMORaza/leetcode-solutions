class Solution:
    def maxRepOpt1(self, text: str) -> int:
        max_length = 0
        character_counts = [0] * 26
        segments_list = []
        for char in text:
            character_counts[ord(char) - ord('a')] += 1
        segments_list.append([text[0], 1])
        for index in range(1, len(text)):
            if text[index] == text[index - 1]:
                segments_list[-1][1] += 1
            else:
                segments_list.append([text[index], 1])
        for segment_char, segment_length in segments_list:
            max_length = max(max_length, min(segment_length + 1, character_counts[ord(segment_char) - ord('a')]))
        for i in range(1, len(segments_list) - 1):
            if segments_list[i - 1][0] == segments_list[i + 1][0] and segments_list[i][1] == 1:
                max_length = max(max_length, min(segments_list[i - 1][1] + segments_list[i + 1][1] + 1,
                                                 character_counts[ord(segments_list[i - 1][0]) - ord('a')]))
        return max_length
