class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        cnt=0
        iszero=False
        for num in nums:
            if num == 0:
                iszero=True
                cnt+=1
            else:
                product *= num
        if (iszero):
            if(cnt>1):
                for i in range(len(nums)):
                    nums[i]=0
                return nums
            else:
                for i in range(len(nums)):
                    if nums[i]==0:
                        nums[i]=product
                    else:
                        nums[i]=0
                return nums
        for i in range (len(nums)):
            nums[i]=product // nums[i]
        return nums