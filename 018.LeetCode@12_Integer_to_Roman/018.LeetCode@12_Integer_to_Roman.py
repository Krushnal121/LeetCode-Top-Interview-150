class Solution:
    def intToRoman(self, num: int) -> str:
        str=""
        while(num>=1000):
            str=str+"M"
            num-=1000
        while(num>=900):
            str=str+"CM"
            num-=900
        while(num>=500):
            str=str+"D"
            num-=500
        while(num>=400):
            str=str+"CD"
            num-=400
        while(num>=100):
            str=str+"C"
            num-=100
        while(num>=90):
            str=str+"XC"
            num-=90
        while(num>=50):
            str=str+"L"
            num-=50
        while(num>=40):
            str=str+"XL"
            num-=40
        while(num>=10):
            str=str+"X"
            num-=10
        while(num>=9):
            str=str+"IX"
            num-=9
        while(num>=5):
            str=str+"V"
            num-=5
        while(num>=4):
            str=str+"IV"
            num-=4
        while(num>=1):
            str=str+"I"
            num-=1
        return str