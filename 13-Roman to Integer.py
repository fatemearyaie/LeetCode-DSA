class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"I": 1,"V": 5,"X": 10,"L": 50,
        "C": 100,"D": 500,"M": 1000}

        previous = 0
        final = 0

        for letter in reversed(s):
            num = roman_values[letter]
            if previous > num:
                final -= num
            elif previous <= num:
                final += num
            previous = num
        return final
       
        
        


