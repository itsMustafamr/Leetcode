from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
            #here int is used to convert length to string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            #here str is used to convert length to string
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            # or res.append(s[j + 1: j + length + 1])
            
        return res
