class Solution:
    """
    Input: 1 array[int]. prices (array[int])
    Output: int. maximum profit (whether you can use
        as many transaction as you want)
    Constrains:
        - NON multiple transactions at the same time
    Edge Cases:

    Time complexity: O(N)
    Space comlpexity: O(1)
    """

    def maxProfit(self, prices: 'List[int]') -> int:
        max_profit = 0

        for key in range(1, len(prices)):
            max_profit += prices[key] - prices[key -
                                               1] if prices[key] > prices[key - 1] else 0

        return max_profit
