class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores (index, height)
        maxarea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                start = index  # this bar extends back to where taller bar was
                maxarea = max(maxarea, height * (i - index))
            stack.append((start, h))
        
        for start, height in stack:
            maxarea = max(maxarea, height * (len(heights) - start))
        
        return maxarea