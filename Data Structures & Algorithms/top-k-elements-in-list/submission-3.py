class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        solution = []
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        for i in range(k):
            max = 0
            for num in seen:
                if seen[num] > max:
                    max_num = num
                    max = seen[num]
            solution.append(max_num)
            del seen[max_num]
        return solution

