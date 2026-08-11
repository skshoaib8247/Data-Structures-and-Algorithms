class Solution:
    def maxDepth(self, s: str) -> int:
      maxi =0
      d=0
      for i in s:
        if i=="(":
            d+=1
        if i==")":
            d-=1
        maxi=max(d,maxi)
      return maxi

#valid parantesis
# Matching pairs
# ( ( ) ( ( ) ) )
#   ↑ ↑       ↑