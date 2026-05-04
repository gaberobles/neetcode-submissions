class Solution:

    def encode(self, strs: List[str]) -> str:
        solution = ""
        for word in strs:
            solution += str(len(word)) + '#' + word
  
        return solution

    def decode(self, s: str) -> List[str]:
        length = ""
        solution = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                solution.append(s[i+1:i+1+int(length)])
                i += 1+int(length)
                length = ""
            else:
                length += s[i]
                i += 1
        return solution