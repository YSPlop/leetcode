def lengthOfLongestSubstring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """

    seen = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Check if the current character has been seen before.
        if s[right] in seen:
            # If it has been seen, move the left pointer to the right of the last occurrence.
            left = max(left, seen[s[right]] + 1)

        # Update the maximum length.
        max_length = max(max_length, right - left + 1)

        # Store the last occurrence of the current character.
        seen[s[right]] = right

    return max_length


if __name__ == "__main__":
    print("abcabcbb length is",lengthOfLongestSubstring("abcabcbb"))
    print("bbbbb length is",lengthOfLongestSubstring("bbbbb"))
    print("pwwkew length is",lengthOfLongestSubstring("pwwkew"))
    print("dvdf length is",lengthOfLongestSubstring("dvdf"))
    print("au length is",lengthOfLongestSubstring("au"))
    print("aab length is",lengthOfLongestSubstring("aab"))
    print("abba length is",lengthOfLongestSubstring("abba"))
    