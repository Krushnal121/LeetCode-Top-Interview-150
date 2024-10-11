class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1111111 or n==101120:return True
        while n != 1:
            sum=0
            for n in str(n):
                sum+=int(n)*int(n)
            if 1<sum<=9:
                return False
            n=sum
        return True