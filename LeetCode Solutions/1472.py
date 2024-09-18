class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.forward_stack = []
        self.current = homepage
    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forward_stack = []
        self.current = url
    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:
            self.forward_stack.append(self.history.pop())
            steps -= 1
        self.current = self.history[-1]
        return self.current
    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.history.append(self.forward_stack.pop())
            steps -= 1
        self.current = self.history[-1]
        return self.current
