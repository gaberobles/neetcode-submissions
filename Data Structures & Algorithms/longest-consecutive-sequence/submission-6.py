class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        sequence = []
        maxcount = 0
        for num in nums:
            if num-1 not in nums:
                current = num
                sequence.append(num)
                while current+1 in nums:
                    sequence.append(current+1)
                    current += 1
                maxcount = max(maxcount, len(sequence))
                sequence.clear()
        return maxcount
