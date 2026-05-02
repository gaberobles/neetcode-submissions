class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)): #iterate though dict
            if dict.get(target - nums[i]) != None: #if the difference exists in the dictionary
                return [dict.get(target - nums[i]), i] #return [the index of the difference, followed by the index of the current number]
            dict[nums[i]] = i #if not, then add the key/value pair
        print(dict)