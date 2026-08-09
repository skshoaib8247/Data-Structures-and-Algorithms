class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        c=0
        total=""
        for ch in s:
            if ch=="(":
                c+=1
                res+=ch
            if ch==")":
                c-=1
                res+=ch
            if c==0:
                    #   total = total.replace(resu[i],"") --->#It removes every (, not just the first one.
                       res= res.removeprefix("(")
                       res=res.removesuffix(")") 
                       total+= res #we do this at end because to not disturb the total string after outcomeres
                       res=""
        return total

    # if c == 0:
    #         res.pop(0)      # remove first '('
    #         res.pop()       # remove last ')'

    #         resu += "".join(res)
    #         res = []
    #    if c == 0:
    #             resu += res[1:-1]   # remove first and last
    #             res = ""
