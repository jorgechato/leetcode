class Solution:
    """
    Input: 2 strings. J (string), S (string)
    Output: 1 int. number of jewels (whether S[n] in J)
    Constrains:
        - case sensitive
    Edge Cases:

    Time complexity: O(N^2)
    Space complexity: O(1)
    """
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        return len([stone for stone in S if stone in J])