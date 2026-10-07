class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_number = 0
        cp_number = x
        while x > 0:
            last_digit = x % 10
            x //= 10
            reversed_number = reversed_number * 10 + last_digit

        if reversed_number == cp_number:
            return True
        return False