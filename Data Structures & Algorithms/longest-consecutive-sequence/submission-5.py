class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        sequence = []
        maxcount = 0
        for num in nums:
            if num-1 not in nums:
                sequence.append(num)
                while max(sequence)+1 in nums:
                    sequence.append(max(sequence)+1)
                maxcount = max(maxcount, len(sequence))
                sequence.clear()
        return maxcount
