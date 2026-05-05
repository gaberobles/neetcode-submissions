class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        for i in range(len(nums)-1):
            prefix[i+1] = prefix[i]*nums[i]
        i = len(nums)-1 #3
        while i > 0:
            postfix[i-1] = postfix[i]*nums[i]
            i -= 1
        return [a*b for a, b in zip(prefix, postfix)]

