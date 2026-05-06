class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        i = 0
        while i < len(nums)-1:
            j, k = i+1, len(nums)-1
            while j < k :
                if nums[j] + nums[k] == -nums[i]:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:  # skip duplicates
                        j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
            i += 1
            while i < len(nums)-1 and nums[i] == nums[i-1]:  # skip duplicates
                i += 1
        return triplets
