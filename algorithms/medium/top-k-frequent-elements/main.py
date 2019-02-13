class Solution:
    """
    Input: 1 array, 1 int. nums (array), k (int)
    Output: array (of k most frequent elements in nums)
    Constrains:
        - k valid
        - k > 0 and k <= len(nums)
        - Time complexity better O(n log n)
    Edge cases:
        - len(nums) == 0
    """

    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        nums_score = {}

        for key, val in enumerate(nums):
            nums_score[val] = nums_score[val] + 1 if val in nums_score else 1

        return sorted(
            nums_score,
            key=nums_score.get,
            reverse=True,
        )[:k]
