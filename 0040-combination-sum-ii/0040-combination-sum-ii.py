class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        ans = []

        def getRecursion(index, target, ds):
            if target == 0:
                ans.append(list(ds))
                return
            for i in range(index, n):
                if index < i and candidates[i] == candidates[i - 1]:
                    continue
                if target < candidates[i]:
                    break

                ds.append(candidates[i])
                getRecursion(i + 1, target - candidates[i], ds)
                ds.pop()
        
        candidates.sort()
        getRecursion(0, target, [])
        return ans