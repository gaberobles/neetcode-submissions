class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, 1

        while l < r:
            r = l + 1
            while r < len(nums):
                print(l, r)
                if nums[l] == nums[r]:
                    return nums[l]
                r += 1
            l += 1
