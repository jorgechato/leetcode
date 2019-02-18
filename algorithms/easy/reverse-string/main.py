class Solution:
    """
    Input: 1 array. s (array)
    Output: Nan
    Constrain:
    Edge cases:

    Time complexity: O(N)
    Space complexity: O(1)
    """
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        for key in range(int(len(s)/2)):
            s[key], s[len(s)-1-key] = s[len(s)-1-key], s[key]