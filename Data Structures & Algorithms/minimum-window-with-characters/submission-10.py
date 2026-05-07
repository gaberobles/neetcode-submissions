class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tCount = {}
        for char in t:
            tCount[char] = tCount.get(char, 0) + 1

        sCount = {}
        subMatch = 0
        shortest = [0, 1001]

        l = 0
        for r in range(len(s)):
            if s[r] in tCount:
                sCount[s[r]] = sCount.get(s[r], 0) + 1
                if sCount[s[r]] == tCount[s[r]]:
                    subMatch += 1

            while subMatch == len(tCount):
                if r-l < shortest[1]-shortest[0]:
                    shortest[0], shortest[1] = l, r
                if s[l] in sCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        subMatch -= 1
                    if sCount[s[l]] == 0:
                        del sCount[s[l]]
                l += 1

        if shortest == [0, 1001]:
            return ""
        else:
            return s[shortest[0]:shortest[1]+1]