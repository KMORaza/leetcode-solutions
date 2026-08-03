class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        bucket = [0] * k
        result = float('inf')
        
        def backtrack(index):
            nonlocal result
            if index == n:
                result = min(result, max(bucket))
                return
            
            if max(bucket) >= result:
                return
            
            for i in range(k):
                bucket[i] += cookies[index]
                backtrack(index + 1)
                bucket[i] -= cookies[index]
                
                if bucket[i] == 0:
                    break
        
        backtrack(0)
        return result
