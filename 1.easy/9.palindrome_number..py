def isPalindrome(x: int) -> bool:

   return str(x) == str(x)[::-1]

    

print("121", isPalindrome(121))
print("-121", isPalindrome(-121))
print("10", isPalindrome(10))
print("123", isPalindrome(123))
print("1234", isPalindrome(1234))
print("12345", isPalindrome(12345))