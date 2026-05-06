class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        area = 0
        while i < j:
            area = max(area, ((j-i)*(min(heights[i], heights[j]))))
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return area

        