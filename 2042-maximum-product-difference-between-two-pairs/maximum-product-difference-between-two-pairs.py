class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        small1 = small2 = float('inf')
        large1 = large2 = float('-inf')

        for num in nums:
            if num < small1:
                small2 = small1
                small1 = num
            elif num < small2:
                small2 = num

            if num > large1:
                large2 = large1
                large1 = num
            elif num > large2:
                large2 = num

        return (large1 * large2) - (small1 * small2)