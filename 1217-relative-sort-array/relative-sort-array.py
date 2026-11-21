class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        index = 0
        for num in arr2:
            for i in range(len(arr1)):
                if arr1[i] == num:
                    arr1[index], arr1[i] = arr1[i], arr1[index]
                    index += 1
        
        for i in range(index, len(arr1)):
            min_idx = i

            for j in range(i + 1, len(arr1)):
                if arr1[j] < arr1[min_idx]:
                    min_idx = j
            arr1[i], arr1[min_idx] = arr1[min_idx], arr1[i]
        return arr1