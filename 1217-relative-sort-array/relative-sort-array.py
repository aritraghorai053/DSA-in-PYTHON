
class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        index = 0

        for num in arr2:
            for i in range(len(arr1)):
                if arr1[i] == num:
                    arr1[index], arr1[i] = arr1[i], arr1[index]
                    index += 1

        # Selection sort remaining elements
        for i in range(index, len(arr1)):
            min_index = i

            for j in range(i + 1, len(arr1)):
                if arr1[j] < arr1[min_index]:
                    min_index = j

            arr1[i], arr1[min_index] = arr1[min_index], arr1[i]

        return arr1
