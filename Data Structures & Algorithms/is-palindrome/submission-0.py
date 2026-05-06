class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = ""
        for char in s:
            if char.isalnum():
                sc += char.lower()
        i = 0
        j = len(sc)-1
        while i < len(sc)//2:
            if sc[i] != sc[j]:
                return False
            i += 1
            j -= 1
        return True