class Solution:
    def myAtoi(self, s: str) -> int:

        # step 1: ignore leading whitespace

        s = s.lstrip()

        # Step 2: check if the number is negative or positive

        sign = 1
        if s and (s[0] == '-' or s[0] == '+'):
            if s[0] == '-':
                sign = -1

            s = s[1:]

        # Step 3:  Read digits until a non-digit character is encoutered

        i = 0

        while i <  len(s) and s[i].isdigit():
            i += 1

        # Step 4: Convert the digits into an integer

        digits = s[:i]
        if not digits:
            return 0


        num = int(digits) * sign

        # Step 5:  Clamp the integer if it is out of the 32-bit range

        INT_MIN = -2**31

        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN

        elif num > INT_MAX:
            return INT_MAX

        # Step 6: Return the final result

        return num

# example 
sol = Solution()
s = " 4337 my words"
t = "  -5673 i went to the market and bought 42 oranges "
ans = sol.myAtoi(s)
ans2 = sol.myAtoi(t)
print(ans2)
print(ans)
