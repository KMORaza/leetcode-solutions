import re
class Solution:
    @staticmethod
    def is_tag_valid(tag: str) -> bool:
        return 1 <= len(tag) <= 9 and tag.isupper()
    @staticmethod
    def isValid(code: str) -> bool:
        tags = []
        i = 0
        n = len(code)
        while i < n:
            if code.startswith("<![CDATA[", i):
                cdata_end = code.find("]]>", i + 9)
                if cdata_end < 0:
                    return False
                i = cdata_end + 3
            elif code.startswith("</", i):
                tag_start = i + 2
                tag_end = code.find('>', tag_start)
                if tag_end < 0:
                    return False
                tag = code[tag_start:tag_end]
                if not Solution.is_tag_valid(tag) or not tags or tags[-1] != tag:
                    return False
                tags.pop()
                i = tag_end + 1
            elif code[i] == "<":
                tag_start = i + 1
                tag_end = code.find('>', tag_start)
                if tag_end < 0:
                    return False
                tag = code[tag_start:tag_end]
                if not Solution.is_tag_valid(tag):
                    return False
                tags.append(tag)
                i = tag_end + 1
            else:
                i += 1
        return len(tags) == 0


