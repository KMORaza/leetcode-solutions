from typing import List, Dict, Set
class ThroneInheritance:
    def __init__(self, kingName: str):
        self.tree: Dict[str, List[str]] = {kingName: []}
        self.dead: Set[str] = set()
        self.order: List[str] = [kingName]
    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.tree:
            self.tree[parentName].append(childName)
            self.order.append(childName)
            self.tree[childName] = []
    def death(self, name: str) -> None:
        self.dead.add(name)
    def getInheritanceOrder(self) -> List[str]:
        result = []
        def dfs(name: str):
            if name not in self.dead:
                result.append(name)
            for child in self.tree[name]:
                dfs(child)
        dfs(next(iter(self.tree)))
        return result
