class TextEditor:
    def __init__(self):
        self.text = []
        self.cursor = 0
    def addText(self, text: str) -> None:
        self.text[self.cursor:self.cursor] = text
        self.cursor += len(text)
    def deleteText(self, k: int) -> int:
        deleted_count = min(k, self.cursor)
        self.cursor -= deleted_count
        del self.text[self.cursor:self.cursor + deleted_count]
        return deleted_count
    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        return self.getCurrentText()
    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.text), self.cursor + k)
        return self.getCurrentText()
    def getCurrentText(self) -> str:
        return ''.join(self.text[max(0, self.cursor - 10):self.cursor])
