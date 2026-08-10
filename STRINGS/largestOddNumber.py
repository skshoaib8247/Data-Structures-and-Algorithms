class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""
        # maxi=0
        # if int(num)%2!=0:
        #     return num
        # else :
        #     for i in num:
        #         if int(i)%2!=0:
        #             maxi=max(maxi,int(i))
        # if maxi %2==0:
        #     return "" 
        # return str(maxi)
