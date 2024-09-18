class Solution:
    def entityParser(self, text: str) -> str:
        entity_map = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": '&',
            "&gt;": '>',
            "&lt;": '<',
            "&frasl;": '/'
        }
        for entity, char in sorted(entity_map.items(), key=lambda x: len(x[0]), reverse=True):
            if entity == "&amp;":
                continue
            text = text.replace(entity, char)
        text = text.replace("&amp;", '&')
        return text
