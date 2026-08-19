# class Solution:
#     def reverseWords(self, s: str) -> str:
#         l=s.split()
#         l.reverse()
#         l=" ".join(l)
#         return l

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         res=""
#         l=s.split()
#         for i in range(len(l)-1,-1,-1):
#             res+=l[i]
#             res+=" "#will not work as last space is added
#         return res
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s=s[::-1]
        s=" ".join(s)
        return s