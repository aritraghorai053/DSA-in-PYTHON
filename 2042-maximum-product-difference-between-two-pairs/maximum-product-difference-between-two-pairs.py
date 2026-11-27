class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)


        w = nums[0]
        x = nums[1]
        y = nums[n-2]
        z = nums[n-1]

        return (y * z) - (w * x)