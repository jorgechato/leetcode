class Solution:
    """
    Input: 1 array. a (array)
    Output: int (len(longest word chain))
    Constrains:
        - valid chain is:
          - left word [-1] == right word[0]
    Edge Cases:

    Time complexity: O(N^2)
    Space complexity: O(N)
    """

    def string_chain(self, a):
        dic = {}
        dic[0] = ""
        key = 0

        for val in a:
            if self.valid_chain(dic[key], val):
                dic[key] += val[-1]
            else:
                key += 1
                dic[key] = val[-1]

        return len(self.longest_chain(dic))

    def longest_chain(self, dic):
        return sorted(
            dic.values(),
            key=lambda x: len(x),
            reverse=True
        )[0]

    def valid_chain(self, l, r):
        return True if len(l) == 0 or r[0] == l[-1] else False


print(
    Solution().string_chain([
        "the",
        "eats",
        "snakes",
        "the",
        "eagle",
        "eats",
        "snakes",
    ]),
)
