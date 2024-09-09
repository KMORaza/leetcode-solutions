class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            email_to_name[first_email] = name
            uf.add(first_email)
            for email in account[2:]:
                email_to_name[email] = name
                uf.add(email)
                uf.union(first_email, email)
        root_to_emails = {}
        for email in email_to_name:
            root = uf.find(email)
            if root not in root_to_emails:
                root_to_emails[root] = []
            root_to_emails[root].append(email)
        result = []
        for root, emails in root_to_emails.items():
            name = email_to_name[root]
            sorted_emails = sorted(emails)
            result.append([name] + sorted_emails)
        return result
