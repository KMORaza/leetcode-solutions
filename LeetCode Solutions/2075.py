class Solution:
    def decodeCiphertext(self, cipherText: str, numRows: int) -> str:
        outputCharacters = []
        totalColumnsCount = len(cipherText) // numRows
        for initialColumn in range(totalColumnsCount):
            for currentRowIndex, currentColumnIndex in zip(range(numRows), range(initialColumn, totalColumnsCount)):
                if currentRowIndex < numRows and currentColumnIndex < totalColumnsCount:
                    outputCharacters.append(cipherText[currentRowIndex * totalColumnsCount + currentColumnIndex])
        finalOutput = ''.join(outputCharacters).rstrip()
        return finalOutput
