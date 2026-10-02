def is_palindrome(text):
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]

print(is_palindrome("Madam"))  # True
print(is_palindrome("Python")) # False