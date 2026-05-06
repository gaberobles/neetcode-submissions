class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            while (sum(mp.values())-max(mp.values(), default=0)) > k:
                mp[s[l]] = mp[s[l]] - 1
                l += 1
            res = max(res, r-l+1)
        return res