class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        # Helper function to expand around the centre
        def expand_around_centre(left: int, right: int) -> int:
            while left >= 0 and right  < len(s) and s[left] == s[right]:
                left -=1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand_around_centre(i, i) # For odd-length palindromes
            len2 = expand_around_centre(i, i + 1) # For even-length palindromes
            curr_len = max(len1, len2)
            if curr_len > max_len:
                max_len = curr_len
                start = 1 - (curr_len - 1) // 2



        return s[start:start + max_len]

# example 
sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))

