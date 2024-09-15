import random
class SkipNode:
    def __init__(self, output, next=None, down=None):
        self.output = output
        self.next = next
        self.down = down
class Skiplist:
    def __init__(self):
        self.dummy = SkipNode(-1)
    def search(self, target):
        node = self.dummy
        while node:
            node = self.advance(node, target)
            if node.next and node.next.output == target:
                return True
            node = node.down
        return False
    def add(self, num):
        nodes = []
        node = self.dummy
        while node:
            node = self.advance(node, num)
            nodes.append(node)
            node = node.down
        down = None
        should_insert = True
        while should_insert and nodes:
            prev = nodes.pop()
            prev.next = SkipNode(num, prev.next, down)
            down = prev.next
            should_insert = random.random() < 0.5
        if should_insert:
            self.dummy = SkipNode(-1, None, self.dummy)
    def erase(self, num):
        found = False
        node = self.dummy
        while node:
            node = self.advance(node, num)
            if node.next and node.next.output == num:
                node.next = node.next.next
                found = True
            node = node.down
        return found
    def advance(self, node, target):
        while node.next and node.next.output < target:
            node = node.next
        return node
