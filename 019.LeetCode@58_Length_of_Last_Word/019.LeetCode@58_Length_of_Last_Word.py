class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        x = i
        while x >= 0 and s[x] != " ":
            x -= 1
        return i - x