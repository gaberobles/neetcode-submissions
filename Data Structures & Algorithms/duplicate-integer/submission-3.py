class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numdict = {}
        for num in nums:
            if num in numdict:
                return True
            else:
                numdict[num] = 1
        return False
