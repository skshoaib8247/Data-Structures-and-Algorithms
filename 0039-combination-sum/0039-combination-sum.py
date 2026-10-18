class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        def fun(index,subset,total):
            if total==target:
                res.append(subset.copy())
                return
            if index==len(candidates) or total>target:
                return 
            subset.append(candidates[index])
            fun(index,subset,total+candidates[index])
            subset.pop()
            fun(index+1,subset,total)
        fun(0,[],0)
        return res