def isPalindrome(s:str) -> bool:
        return s == s[::-1]

def longestPalindrome(s: str) -> str:
    
    result = 0
    current_palindrome = ""
    final_palindrome = ""

    for extract_length in range(len(s), 1, -1):
        
        for i in range(len(s)):
            if i + extract_length > len(s):
                break
            current_palindrome = s[i:i+extract_length]
            if self.isPalindrome(current_palindrome):
                if len(current_palindrome) > result:
                    result = len(current_palindrome)
                    final_palindrome = current_palindrome
                    return final_palindrome
                break
    
    if result < 2:
        return s[0]
    else: 
        return final_palindrome

print("cbbd", longestPalindrome("cbbd"))
print("babad", longestPalindrome("babad"))
print("cbbd", longestPalindrome("cbbd"))

