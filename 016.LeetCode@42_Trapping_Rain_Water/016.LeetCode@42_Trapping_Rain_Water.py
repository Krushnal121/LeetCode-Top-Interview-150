class Solution:
    def trap(self, height: List[int]) -> int:
        sum=0
        if max(height)==min(height):return sum
        length=len(height)
        leftMax=[0]*length
        rightMax=[0]*length
        leftMax[0]=height[0]
        rightMax[-1]=height[-1]
        for i in range (1,length,1):
            leftMax[i]=max(height[i],leftMax[i-1])
        for i in range (length-2,-1,-1):
            rightMax[i]=max(height[i],rightMax[i+1])
        for i in range (1,length,1):
            sum+=(min(leftMax[i],rightMax[i])-height[i])

        return sum