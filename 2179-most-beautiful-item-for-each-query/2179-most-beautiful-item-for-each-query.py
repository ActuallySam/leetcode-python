class Solution(object):
    def binarysearch(self, items, query):
        # Using binary search to find the highest price <= query
        low, high = 0, len(items) - 1
        max_beauty = 0

        while low <= high:
            mid = (low + high) // 2
            if items[mid][0] <= query:
                # Move right if the price at mid is <= query
                max_beauty = max(max_beauty, items[mid][1])
                low = mid + 1
            else:
                # Move left if the price at mid is greater than query
                high = mid - 1

        return max_beauty

    def maximumBeauty(self, items, queries):
        # Step 1: Sort items by price
        items.sort(key=lambda x: x[0])

        # Step 2: Update items with max beauty for each price
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])

        # Step 3: Process each query using binary search
        result = []
        for query in queries:
            result.append(self.binarysearch(items, query))

        return result