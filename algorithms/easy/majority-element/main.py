class Solution:
    """
    Input: 1 array[int]. nums (array[int])
    Output: int, (whether number that appears more than n/2)
    Constrains:
        - non-empty nums
        - majority element always exist
    Edge Cases:

    Time complexity: O(N)
    Space complexity: O(N)
    """

    def majorityElement(self, nums: 'List[int]') -> 'int':
        nums_count = {}

        for val in nums:
            nums_count[val] = nums_count.get(val, 0) + 1

        return sorted(
            nums_count,
            key=nums_count.get
        )[-1]
