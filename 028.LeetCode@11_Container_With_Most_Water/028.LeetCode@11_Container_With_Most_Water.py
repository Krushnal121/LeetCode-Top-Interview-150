class Solution:
    def maxArea(self, height: List[int]) -> int:
        (maxWater,lp,rp)=(0,0,len(height)-1)
        while(lp<rp):
            ht=min(height[lp],height[rp])
            width=rp-lp
            currWater=ht*width
            maxWater=max(maxWater,currWater)
            if (height[lp]<=ht):
                lp+=1
            else:
                rp-=1
        return maxWater