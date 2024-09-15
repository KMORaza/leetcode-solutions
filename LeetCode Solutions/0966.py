from typing import List
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def get_vowel_replaced(word: str) -> str:
            return word.translate(str.maketrans("aeiou", "aaaaa"))
        exact_set = set(wordlist)
        case_insensitive_dict = {}
        vowel_replacement_dict = {}
        vowels = "aeiou"
        for word in wordlist:
            exact_set.add(word)
            lower_word = word.lower()
            if lower_word not in case_insensitive_dict:
                case_insensitive_dict[lower_word] = word
            vowel_replaced = get_vowel_replaced(word.lower())
            if vowel_replaced not in vowel_replacement_dict:
                vowel_replacement_dict[vowel_replaced] = word
        result = []
        for query in queries:
            if query in exact_set:
                result.append(query)
            else:
                lower_query = query.lower()
                if lower_query in case_insensitive_dict:
                    result.append(case_insensitive_dict[lower_query])
                else:
                    vowel_replaced_query = get_vowel_replaced(lower_query)
                    if vowel_replaced_query in vowel_replacement_dict:
                        result.append(vowel_replacement_dict[vowel_replaced_query])
                    else:
                        result.append("")
        return result
