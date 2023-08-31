class Solution:
    
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return (nums)

nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums,k))
