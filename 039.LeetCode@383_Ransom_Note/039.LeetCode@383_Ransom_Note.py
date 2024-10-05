class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = [0] * 26
        for char in ransomNote:
            i = magazine.find(char, letters[ord(char) % 26])
            if i == -1: return False
            letters[ord(char) % 26] = i + 1
        return True