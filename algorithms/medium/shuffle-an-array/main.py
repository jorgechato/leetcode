import random


class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: N
    """

    def __init__(self, nums: 'List[int]'):
        self.nums = nums

    def reset(self) -> 'List[int]':
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> 'List[int]':
        """
        Returns a random shuffling of the array.
        """
        return sorted(
            self.nums,
            key=lambda x: random.random(),
        )


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
