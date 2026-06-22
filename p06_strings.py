def count_char(text, target):
    count = 0
    for i in text:
        if i == target: count += 1
    return count

def remove_spaces(text):
    result = ""
    for i in text: 
        if i != " ": result += i
    return result

def is_palindrome(text):
    test = remove_spaces(text.upper())
    return test ==  test[::-1]

if __name__ == "__main__":
    assert count_char("banana", "a") == 3
    assert remove_spaces("a b  c") == "abc"
    assert is_palindrome("level") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("python") is False