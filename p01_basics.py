def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def rectangle_area(width, height):
    return width * height

def average_three(a, b, c):
    return ( a + b + c ) / 3

if __name__ == "__main__":
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert rectangle_area(3, 4) == 12
    assert average_three(3, 6, 9) == 6
    print("all tests passed")