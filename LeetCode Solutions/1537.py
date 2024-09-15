class Solution:
    def maxSum(self, array1, array2):
        x = 1000000007
        total_sum = 0
        running_sum1 = 0
        running_sum2 = 0
        index1, index2 = 0, 0
        while index1 < len(array1) and index2 < len(array2):
            if array1[index1] < array2[index2]:
                running_sum1 += array1[index1]
                index1 += 1
            elif array1[index1] > array2[index2]:
                running_sum2 += array2[index2]
                index2 += 1
            else:
                total_sum += max(running_sum1, running_sum2) + array1[index1]
                running_sum1 = 0
                running_sum2 = 0
                index1 += 1
                index2 += 1
        while index1 < len(array1):
            running_sum1 += array1[index1]
            index1 += 1
        while index2 < len(array2):
            running_sum2 += array2[index2]
            index2 += 1
        return (total_sum + max(running_sum1, running_sum2)) % x