import re
class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(r"""
            ^                        
            [+-]?                      
            (                        
                (\d+(\.\d*)?)        
                |                   
                (\.\d+)                
            )                        
            ([eE][+-]?\d+)?           
            $                        
        """, re.VERBOSE)
        return pattern.match(s) is not None