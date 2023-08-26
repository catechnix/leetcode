from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums), nums


nums = [1, 2, 1, 2, 3, 2, 4, 5]
num = Solution().removeDuplicates(nums)
print(num)
print(nums)
