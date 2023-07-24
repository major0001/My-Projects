class Solution:

    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
                len1 = expand_around_center(i, i) # for odd-length palindromes
                len2 = expand_around_center(i, i + 1) # for even-length palindromes

                curr_len = max(len1, len2)

                if curr_len > max_len:
                   max_len = curr_len

                   start = i - (curr_len - 1) // 2

        return s[start:start + max_len]

# examples
sol = Solution()
s1 = "caaag"
s2 = "barber"
s3 = "sister"
ans = sol.longestPalindrome(s1)
ans2 = sol.longestPalindrome(s2)
ans3 = sol.longestPalindrome(s3)

print(ans)
print(ans2)
print(ans3)
