class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashset = set([i for i in range(1, n+1)])
        nums_set = set(nums)
        diff = hashset.difference(nums_set)
        return list(diff)
