class Solution:
    """
    Input: 1 string. s (string)
    Output: 1 string. (whether the vowles are reverse)
    Constrains:
        - s is a valid string
    Edge Cases:
        - len(s) == 0
        - wovles no in s
        - len(wovles) == 1

    Time complexity: O(N^2)
    Space complexity: O(1)
    """
    def reverseVowels(self, s: 'str') -> 'str':
        vowles = ""

        for c in s:
            if self.is_vowle(c):
                vowles += c

        revers = ""
        key = 0 

        for c in s:
            if len(vowles) > key and c.lower() == vowles[key].lower():
                revers += vowles[len(vowles)-1-key]
                key += 1
            else:
                revers += c

        return revers

    def is_vowle(self, c):
        """
        Helper function to indentify is a
        character is a vowel.
        """
        return True if c.lower() in "aeiou" else False