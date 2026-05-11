class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    # left is sorted and target is in between these two
                    r = m-1
                else:
                    # left is sorted but target not inside
                    l = m+1
            else:
                if nums[m] <= target <= nums[r]:
                    # right is sorted and target is in between these two
                    l = m+1
                else:
                    # right is sorted but target not inside
                    r = m-1

        return -1