class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        sol=[]
        for i in range(numRows):
            sol.append([])
        idx=0
        idxlst=0
        increment=1
        while idx<len(s):
            while(idxlst<numRows and idxlst>-1 and idx<len(s)):
                sol[idxlst].append(s[idx])
                idxlst+=increment
                idx+=1
            increment*=-1
            idxlst+=increment
            idxlst+=increment
        ans=""
        for i in sol:
            ans+="".join(i)
        return ans