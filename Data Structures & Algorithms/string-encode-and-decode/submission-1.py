class Solution:

    def encode(self, strs: List[str]) -> str:
        solution = ""
        for word in strs:
            solution += word + "."
        return solution

    def decode(self, s: str) -> List[str]:
        current = ""
        solution = []
        for char in s:
            if char == '.':
                solution.append(current)
                current = ""
            else:
                current += char
        return solution