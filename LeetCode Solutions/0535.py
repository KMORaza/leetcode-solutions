import string
import random
class Codec:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"
        self.alphabet = string.ascii_letters + string.digits
        self.code_length = 6
    def encode(self, longUrl: str) -> str:
        code = self._generate_code()
        while code in self.code_to_url:
            code = self._generate_code()
        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl
        return self.base_url + code
    def decode(self, shortUrl: str) -> str:
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")
    def _generate_code(self) -> str:
        return ''.join(random.choices(self.alphabet, k=self.code_length))
