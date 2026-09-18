class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  # sort to handle duplicates easily

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # prune if current number exceeds remaining target
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i+1, path, remaining - candidates[i])  # move to next index
                path.pop()

        backtrack(0, [], target)
        return res
