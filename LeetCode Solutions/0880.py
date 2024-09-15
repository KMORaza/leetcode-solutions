class Solution:
    def decodeAtIndex(self, encoded_string: str, index: int) -> str:
        decoded_length = 0
        for char in encoded_string:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1
        for i in reversed(range(len(encoded_string))):
            index %= decoded_length
            if index == 0 and encoded_string[i].isalpha():
                return encoded_string[i]
            if encoded_string[i].isdigit():
                decoded_length //= int(encoded_string[i])
            else:
                decoded_length -= 1
        raise ValueError("Invalid index value")
