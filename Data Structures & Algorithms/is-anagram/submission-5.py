class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sdict = {}
        for char in s:
            sdict[char] = sdict.get(char, 0) + 1
        
        for char in t:
            if char not in sdict:
                return False
            sdict[char] -= 1
            if sdict[char] == 0:
                del sdict[char]
        
        return len(sdict) == 0