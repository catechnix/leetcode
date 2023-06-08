grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        count =0
        for r in grid:
            for i in r:
                if i < 0:
                    count +=1
        return count

solution = Solution()
total_count=solution.countNegatives(grid)
print(total_count)

