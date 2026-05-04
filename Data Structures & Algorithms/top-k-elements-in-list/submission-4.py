class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = Counter(nums)
        return [num for num, count in seen.most_common(k)]

