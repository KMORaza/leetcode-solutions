class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        def one(num):
            lookup = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                      "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                      "Eighteen", "Nineteen"]
            return lookup[num]
        def ten(num):
            lookup = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            return lookup[num // 10] + ("" if num % 10 == 0 else " " + one(num % 10))
        def two(num):
            if num == 0:
                return ""
            elif num < 20:
                return one(num)
            elif num < 100:
                return ten(num)
            else:
                return one(num // 100) + " Hundred" + ("" if num % 100 == 0 else " " + two(num % 100))
        def three(num):
            billion = num // 1000000000
            million = (num % 1000000000) // 1000000
            thousand = (num % 1000000) // 1000
            remainder = num % 1000
            result = ""
            if billion > 0:
                result += two(billion) + " Billion"
            if million > 0:
                result += ("" if result == "" else " ") + two(million) + " Million"
            if thousand > 0:
                result += ("" if result == "" else " ") + two(thousand) + " Thousand"
            if remainder > 0:
                result += ("" if result == "" else " ") + two(remainder)
            return result
        return three(num).strip()

