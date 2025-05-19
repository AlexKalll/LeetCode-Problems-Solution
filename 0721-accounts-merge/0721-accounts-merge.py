class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, email):
        if self.parent[email] != email:
            self.parent[email] = self.find(self.parent[email])  
        return self.parent[email]
    
    def union(self, email1, email2):
        root1 = self.find(email1)
        root2 = self.find(email2)
        if root1 != root2:
            self.parent[root2] = root1 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in uf.parent:
                uf.parent[first_email] = first_email
            
            for email in account[2:]:
                if email not in uf.parent:
                    uf.parent[email] = email
                uf.union(first_email, email)
        
        # group emails by their root
        email_groups = defaultdict(list)
        for email in uf.parent.keys():
            root = uf.find(email)
            email_groups[root].append(email)
        
        result = []
        for root_email, emails in email_groups.items():
            name = next(account[0] for account in accounts if root_email in account)
            result.append([name] + sorted(emails))
        
        return result
