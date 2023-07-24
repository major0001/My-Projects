class Solution:
    def isPalindrome(self, x: int) -> bool:

        # handle negative numbers
        if x < 0:
            return False

        # extract the digits
        original_x = x
        reversed_x = 0

        while x > 0:
            digit = x % 10
            reversed_x *= 10
            reversed_x += digit
            x //= 10

        # compare the digits
        return original_x == reversed_x

# example 
sol = Solution()
s = sol.isPalindrome(121)
print(s)
