class Encrypter:
    def __init__(self, cipher_keys, cipher_values, input_words):
        self.encryption_map = dict(zip(cipher_keys, cipher_values))
        self.encrypted_count_map = {}
        for word in input_words:
            encoded_word = self.encrypt(word)
            if encoded_word:
                self.encrypted_count_map[encoded_word] = self.encrypted_count_map.get(encoded_word, 0) + 1
    def encrypt(self, word):
        encoded_result = []
        for char in word:
            if char not in self.encryption_map:
                return ""
            encoded_result.append(self.encryption_map[char])
        return ''.join(encoded_result)
    def decrypt(self, encoded_word):
        return self.encrypted_count_map.get(encoded_word, 0)
