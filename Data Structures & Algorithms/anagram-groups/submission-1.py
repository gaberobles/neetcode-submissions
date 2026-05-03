class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = []
        seen = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in seen:
                seen[key] = []
            seen[key].append(strs[i])
        for key in seen:
            solution.append(seen[key])
        return solution