class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l, r = -1, len(nums1)-1 #l and r are the index
        total = len(nums1) + len(nums2)

        while l <= r:
            i = (l+r)//2 #i is index of left of nums1
            j = total//2 - i - 2 #j is index of left of nums2

            maxLeftNums1 = nums1[i] if i >= 0 else float('-inf')
            minRightNums1 = nums1[i+1] if i < len(nums1)-1 else float('inf')
            maxLeftNums2 = nums2[j] if j >= 0 else float('-inf')
            minRightNums2 = nums2[j+1] if j < len(nums2)-1 else float('inf')

            if maxLeftNums1 <= minRightNums2 and maxLeftNums2 <= minRightNums1:
                if total%2: #if odd
                    return min(minRightNums1, minRightNums2)
                else: #if even
                    return (max(maxLeftNums1, maxLeftNums2)+min(minRightNums1, minRightNums2))/2
            elif maxLeftNums1 > minRightNums2:
                r = i-1
            else:
                l = i+1