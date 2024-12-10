def is_palindrome(s):
    return s == s[::-1]

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    print("All tests passed!")

if __name__ == "__main__":
    test_is_palindrome()
