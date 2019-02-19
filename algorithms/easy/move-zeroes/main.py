class Solution:
    """
    Input: 1 string[int]. nums (string[int])
    Output: Nan
    Constrains:
        - nums well formated
        - in-place without making a copy of the array.
    Edge Cases:
        - len(nums) == 0

    Time complexity: O(N)
    Space complexity: O(1)
    """

    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = [x for x in nums if x != 0]

        for key in range(len(nums)):
            if key < len(non_zero):
                nums[key] = non_zero[key]
            else:
                nums[key] = 0
