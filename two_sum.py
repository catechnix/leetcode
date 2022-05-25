class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """       

        idx = 0
        for idx in range(len(nums)):
            while idx < len(nums)-1:
                if nums[idx] + nums[idx+1] == target:
                     print([idx,idx+1])                                 
                idx +=1

s = Solution()
s.twoSum([3,2,4],6)
