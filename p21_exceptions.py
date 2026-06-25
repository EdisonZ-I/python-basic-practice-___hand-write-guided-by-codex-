def safe_divide(a, b):
    try: 
        return a / b
    except:
        return None
    
def parse_int_or_none(text):
    try:
        return int(text)
    except:
        return None
    
if __name__ == "__main__":
    assert safe_divide(6, 2) == 3
    assert safe_divide(6, 0) is None
    assert parse_int_or_none("123") == 123
    assert parse_int_or_none("abc") is None
