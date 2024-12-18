class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        # res = [None] * n
        # res[-1] = prices[-1]

        # for i in range(n):
        #     j = i + 1
        #     price = prices[i]
        #     while j < n:
        #         print(i, prices[j] > prices[i])
        #         if j == n - 1 and prices[j] > prices[i]:
        #             res[i] = prices[i]
        #         elif prices[j] <= prices[i]:
        #             discount = price - prices[j]
        #             res[i] = discount
        #             break

        #         j += 1
        
        # return res

        stack = []
        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                prices[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop()
            stack.append(i)
        return prices

