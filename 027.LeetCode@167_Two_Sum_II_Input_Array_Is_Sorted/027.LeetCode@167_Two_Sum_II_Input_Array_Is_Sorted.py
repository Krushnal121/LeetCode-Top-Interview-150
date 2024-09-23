class Solution:
    def twoSum(self, numbers, target):
        startidx=0
        endidx=len(numbers)-1
        while startidx<endidx:
            if numbers[startidx]+numbers[endidx]==target:
                return [startidx+1,endidx+1]
            elif numbers[startidx]+numbers[endidx]>target:
                endidx -= 1
            else:
                startidx += 1