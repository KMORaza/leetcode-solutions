from typing import List
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)
            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                domain_count[subdomain] += count
        result = [f"{count} {domain}" for domain, count in domain_count.items()]
        return result
