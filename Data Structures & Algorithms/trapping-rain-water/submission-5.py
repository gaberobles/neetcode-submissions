class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        prefix = [0]*len(height)
        pre = 0
        for i in range(len(height)):
            prefix[i] = pre
            pre = max(prefix[i], height[i])
        postfix = [0]*len(height)
        post = 0
        for i in range(len(height)-1, -1, -1):
            postfix[i] = post
            post = max(postfix[i], height[i])
        print(prefix)
        print(postfix)
        for i in range(len(height)):
            area += max(0, min(prefix[i], postfix[i]) - height[i])
        return area