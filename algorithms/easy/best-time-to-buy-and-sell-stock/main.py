class Solution:
    """
    Input: 1 array. prices (array)
    Output: 1 int. max profit (whether max(prices[n] - prices[m]))
    Constrains:
        - max(prices) pos > min(prices) pos
    Edge Cases:

    Time complexity: O(N)
    Space complexity: O(1)
    """
    def maxProfit(self, prices: 'List[int]') -> 'int':
        min_price, max_profit = float('inf'), 0

        for price in prices:
            min_price = price if price < min_price else min_price
            max_profit = price - min_price if price - min_price > max_profit else max_profit

        return max_profit