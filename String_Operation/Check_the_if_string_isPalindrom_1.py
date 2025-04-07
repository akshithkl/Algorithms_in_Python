def is_palindrome(s):
    return s == s[::-1]  # Check if the string is equal to its reverse

# Example
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
