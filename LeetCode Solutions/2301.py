class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mapping_dict = {}
        for old_char, new_char in mappings:
            if old_char not in mapping_dict:
                mapping_dict[old_char] = set()
            mapping_dict[old_char].add(new_char)
        
        sub_len = len(sub)
        s_len = len(s)
        
        for i in range(s_len - sub_len + 1):
            match = True
            for j in range(sub_len):
                s_char = s[i + j]
                sub_char = sub[j]
                
                if s_char == sub_char:
                    continue
                elif sub_char in mapping_dict and s_char in mapping_dict[sub_char]:
                    continue
                else:
                    match = False
                    break
            
            if match:
                return True
        
        return False
