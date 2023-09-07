"""
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

"""

class Solution:
    def hIndex(self, c: list[int]) -> int:
        c.sort(reverse=True)
        if len(c)==1 and c[0]>0:
            return 1
        if c[-1]>=len(c):
            return len(c)
        for i in range(len(c)):
            if c[i]<i+1:
                return i
        
#citations = [3,0,6,1,5]
citations = [3,0,6,1,5,9,10]

print(Solution().hIndex(citations))
