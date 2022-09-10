# Code Solution for leetcode


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # extreme case that lead to dead loop
        if len(prices) == 0 or k == 0:
            return 0

        low = prices[0]
        high = prices[0]
        buy = False
        sell = True
        profit = []
        for i in range(1, len(prices)):
            if prices[i] <= low and buy is False:
                low = prices[i]

            if prices[i] > low and buy is False:
                buy = True
                sell = False
                high = prices[i]

            if prices[i] >= high and sell is False:
                high = prices[i]

            if prices[i] < high and sell is False:
                profit.append((low, high))
                sell = True
                buy = False
                low = prices[i]

        if buy is True and sell is False:
            profit.append((low, high))

        profit_len = len(profit)
        # print(profit)
        cache = {}

        def profit_k(low, high, k):
            if (low, high, k) in cache:
                return cache[(low, high, k)]
            if k >= high - low + 1:
                cache[(low, high, k)] = sum([h - l for l, h in profit[low:high + 1]])
                return cache[(low, high, k)]
            if k == 1:
                buy = profit[low][0]
                sell = profit[low][1]
                i = low + 1
                temp = sell - buy
                while i <= high:
                    if profit[i][0] < buy:
                        buy = profit[i][0]
                        sell = profit[i][1]
                    if profit[i][1] > sell:
                        sell = profit[i][1]
                    if sell - buy > temp:
                        temp = sell - buy
                    i += 1
                cache[(low, high, 1)] = temp
                return temp
            else:
                temp = 0
                for i in range(low, high - k + 2):
                    temp = max(temp, profit_k(low, i, 1) + profit_k(i + 1, high, k - 1))
                cache[(low, high, k)] = temp
                return temp

        return profit_k(0, profit_len - 1, k) if profit_len > 0 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit(0, [1, 3]))