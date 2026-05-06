class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                while s[l] != s[r]:
                    seen.discard(s[l])
                    l += 1
                l += 1
                r += 1
            res = max(res, (r-l))
        return res