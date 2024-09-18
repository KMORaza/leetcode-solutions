from typing import List
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        company_sets = [set(companies) for companies in favoriteCompanies]
        result = []
        for i, companies_i in enumerate(company_sets):
            is_subset = False
            for j, companies_j in enumerate(company_sets):
                if i != j and companies_i.issubset(companies_j):
                    is_subset = True
                    break
            if not is_subset:
                result.append(i)
        return result
