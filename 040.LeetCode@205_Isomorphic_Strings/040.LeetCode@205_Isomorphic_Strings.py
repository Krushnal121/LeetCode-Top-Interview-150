class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        indexS = [0] * 128
        indexT = [0] * 128

        for i in range(len(s)):
            if indexS[ord(s[i])] != indexT[ord(t[i])]:
                return False
            indexS[ord(s[i])] = indexT[ord(t[i])] = i + 1

        return True