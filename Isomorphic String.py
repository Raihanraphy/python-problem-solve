class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_to_t_mapping = {}
        
        t_to_s_mapping = {}
      
        
        for char_s, char_t in zip(s, t):
            
            if char_s in s_to_t_mapping and s_to_t_mapping[char_s] != char_t:
                return False
          
            
            if char_t in t_to_s_mapping and t_to_s_mapping[char_t] != char_s:
                return False
          
            
            s_to_t_mapping[char_s] = char_t
            t_to_s_mapping[char_t] = char_s
      
        
        return True
