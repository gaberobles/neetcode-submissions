class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)): #iterate though dict
            if (target-nums[i]) in seen: #if the difference exists in the dictionary
                return [seen.get(target - nums[i]), i] #return [the index of the difference, followed by the index of the current number]
            seen[nums[i]] = i #if not, then add the key/value pair