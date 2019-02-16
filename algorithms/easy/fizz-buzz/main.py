class Solution:
    """
    Input: 1 int. n (int)
    Output: 1 array. ()
    Constrains:
        - n int
        - n > 0
    Edge cases:
        - n < 1 (not in this case)

    Time complexity: O(N)
    Space complexity: 1
    """

    def fizzBuzz(self, n: 'int') -> 'List[str]':
        return list(
            map(
                lambda x: "FizzBuzz" if x % 3 == 0 and x % 5 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else str(
                    x),
                {x for x in range(1, n+1)},
            )
        )
