class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=start=0
        lastidx=[0]*128
        for end in range(len(s)):
            start=max(start,lastidx[ord(s[end])])
            maxlen=max(maxlen,end-start+1)
            lastidx[ord(s[end])]=end+1
        return maxlen