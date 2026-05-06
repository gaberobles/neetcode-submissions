class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub = Counter(s1)
        seen = {}
        l = 0

        for r in range(len(s2)):
            print(seen)
            seen[s2[r]] = seen.get(s2[r], 0) + 1
            if r-l+1 > len(s1):
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1
            if sub == seen:
                return True
        
        return False