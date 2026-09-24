class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start^goal
        c=0
        while ans:
            ans=ans&ans-1
            c+=1
        return c
