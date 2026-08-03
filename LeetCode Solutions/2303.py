class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total_tax = 0.0
        prev_upper = 0
        
        for upper, percent in brackets:
            if income <= 0:
                break
                
            taxable_income = min(income, upper - prev_upper)
            tax_in_bracket = taxable_income * percent / 100.0
            total_tax += tax_in_bracket
            
            income -= taxable_income
            prev_upper = upper
        
        return total_tax
