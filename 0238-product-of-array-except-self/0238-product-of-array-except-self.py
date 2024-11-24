class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefixProduct, suffixProduct = 1, 1

        for i in range(n):
            res[i] = prefixProduct
            prefixProduct *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] *= suffixProduct
            suffixProduct *= nums[i]
        return res