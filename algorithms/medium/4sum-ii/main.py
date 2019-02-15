from collections import defaultdict


class Solution:
    '''
    Input: 4 arrays. A (array), B (array),C (array), D (array)
    Output: int (number of tuples to sum 0)
    Constrains: len(A) == len(B) == len(C) == len(D), all int
    Edge Cases:

    Time complexity: O(N^2)
    Space complexity: O(N)
    '''

    def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]') -> 'int':
        dic = defaultdict(int)
        ans = 0

        for a in A:
            for b in B:
                dic[a+b] += 1

        for c in C:
            for d in D:
                if -1*(c+d) in dic:
                    ans += dic[-1*(c+d)]

        return ans
