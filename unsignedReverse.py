class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        sign = -1 if x < 0 else 1
        x = abs(x)

        result =  0
        while x > 0:
            result =  result * 10 + x % 10
            x //= 10

        result *= sign

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result

# example 
sol = Solution()
x = 456
ans = sol.reverse(x)
print(ans)


