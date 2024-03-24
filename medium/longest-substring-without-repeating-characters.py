def lengthOfLongestSubstring(s: str) -> int:

    if len(s) == 1:
        return 1 

    current_position = 0
    length = 0
    substring = ""
    max_len = 0
    longest_substring = ""

    for character in s:
        if character not in substring:
            substring += character
            
        else:

            while (character not in s):
                substring = s[current_position: length]
                current_position += 1
                

            if len(substring) > max_len:
                max_len = len(substring)
                longest_substring = substring

        length += 1
    
    print("substring is", longest_substring)
    if len(substring) > max_len:
        return len(substring)
    else:
        return max_len

if __name__ == "__main__":
    print("abcabcbb length is",lengthOfLongestSubstring("abcabcbb"))
    print("bbbbb length is",lengthOfLongestSubstring("bbbbb"))
    print("pwwkew length is",lengthOfLongestSubstring("pwwkew"))
    print("dvdf length is",lengthOfLongestSubstring("dvdf"))
    print("au length is",lengthOfLongestSubstring("au"))
    print("aab length is",lengthOfLongestSubstring("aab"))
    print("abba length is",lengthOfLongestSubstring("abba"))
    