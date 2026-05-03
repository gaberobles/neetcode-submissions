class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for char in s:
            if char not in sdict:
                sdict[char] = 1
            else:
                sdict[char] = sdict[char]+1
        for char in t:
            if len(sdict) == 0:
                return False
            if sdict.get(char) == 1:
                del sdict[char]
            elif char in sdict:
                sdict[char] = sdict.get(char)-1
            else:
                return False
        if len(sdict) == 0:
            return True
        else:
            return False
            