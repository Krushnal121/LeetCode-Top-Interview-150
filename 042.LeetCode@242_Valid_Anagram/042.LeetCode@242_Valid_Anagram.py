class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst=[0]*26
        for i in range(len(s)):
            lst[ord(s[i])-97]+=1
            lst[ord(t[i])-97]-=1
        for i in lst:
            if i != 0:
                return False
        return True
