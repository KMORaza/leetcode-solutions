class Solution:
    def maxProduct(self, s: str) -> int:
        length = len(s)
        result = 1
        oddLengthLeft = self.calculatePalindromes(s, length)
        oddLengthRight = self.calculatePalindromes(s[::-1], length)
        self.reverseArray(oddLengthRight, 0, length - 1)
        for i in range(1, length):
            result = max(result, oddLengthLeft[i - 1] * oddLengthRight[i])
        return result
    def calculatePalindromes(self, s: str, n: int) -> list[int]:
        maxExtensions = [0] * n
        longestPalindromes = [1] * n
        currentCenter = 0
        for i in range(n):
            rightBoundary = currentCenter + maxExtensions[currentCenter] - 1
            mirroredIndex = currentCenter - (i - currentCenter)
            extension = 1 if i > rightBoundary else min(maxExtensions[mirroredIndex], rightBoundary - i + 1)
            while i - extension >= 0 and i + extension < n and s[i - extension] == s[i + extension]:
                longestPalindromes[i + extension] = 2 * extension + 1
                extension += 1
            maxExtensions[i] = extension
            if i + maxExtensions[i] >= rightBoundary:
                currentCenter = i
        for i in range(1, n):
            longestPalindromes[i] = max(longestPalindromes[i], longestPalindromes[i - 1])
        return longestPalindromes
    def reverseArray(self, arr: list[int], left: int, right: int) -> None:
        while left < right:
            self.swapElements(arr, left, right)
            left += 1
            right -= 1
    def swapElements(self, arr: list[int], i: int, j: int) -> None:
        arr[i], arr[j] = arr[j], arr[i]