class Solution:
    """
    Input: 1 string. s (string)
    Output: int (index of first non repeating character)
    Constrains:
        - -1 if char doesn't exist
    Edge Cases:
        - len(s) == 0

    Time complexity: O(N)
    Space complexity: O(N)
    """

    def firstUniqChar(self, s: 'str') -> 'int':
        if len(s) == 0:
            return -1

        chars = list(
            filter(
                lambda x: x != -1,
                self.map_chars(s).values(),
            )
        )

        if len(chars) == 0:
            return -1

        return chars[0]

    def map_chars(self, s):
        chars = {}

        for key, val in enumerate(s):
            if val in chars:
                chars[val] = -1
            else:
                chars[val] = key

        return chars
