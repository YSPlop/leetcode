def longestPalindrome(s: str) -> str:
    """
    Returns the longest palindromic substring in a given string.

    Args:
        s: The string to search for the longest palindrome.

    Returns:
        The longest palindromic substring in s.
    """

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest_palindrome = ""
    for i in range(len(s)):
        # Check for odd-length palindromes
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest_palindrome):
        # Check for even-length palindromes
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest_palindrome):
            longest_palindrome = even_palindrome

    return longest_palindrome
