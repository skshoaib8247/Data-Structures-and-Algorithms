class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s)!=len(goal):
             return False
        for i in range(len(s)):
            if s[-i:]+s[:-i]==goal:
                return True
        return False
           
# """s[-i:] + s[:-i]--->right roatation"""

# """s[i:] + s[:i] ---> left roatation""

# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         for i in s:
#             if i not in goal:# just checks not iterate at every index
#                 return False
#         return True

#this code will fail s = "abcde"
# goal = "abced" altenate postion shuld not change even afte rotation
 