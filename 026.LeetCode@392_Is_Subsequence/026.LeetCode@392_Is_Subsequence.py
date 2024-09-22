class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stridx=subidx=0
        while(stridx<len(t) and subidx<len(s)):
            if t[stridx] == s[subidx]:
                subidx+=1
                stridx+=1
            else:
                stridx += 1
        return subidx==len(s)