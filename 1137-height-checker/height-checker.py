class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = heights.copy()
        n = len(heights)

        for i in range(0, n):
            min_idx = i
            for j in range (i+1, n):
                if expected[j] < expected[min_idx]:
                    min_idx = j
            expected[i], expected[min_idx] = expected[min_idx], expected[i]

        count = 0
        for i in range(0, n):
            if heights[i] != expected[i]:
                count += 1
        return count