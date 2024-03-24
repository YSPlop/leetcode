def lengthOfLongestSubstring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
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
