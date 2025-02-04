class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)
        
        for entry in cpdomains:
            rep, domain = entry.split()
            rep = int(rep)
            parts = domain.split('.')
            
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                count[subdomain] += rep
        
        result = []
        for domain, visits in count.items():
            result.append(f"{visits} {domain}")
        
        return result