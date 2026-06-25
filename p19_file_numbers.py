def read_numbers(path):
    result = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                result.append( int(line.strip()) )
    return result

if __name__ == "__main__":
    with open("numbers_test.txt", "w", encoding="utf-8") as f:
        f.write("1\n\n2\n3\n")

    assert read_numbers("numbers_test.txt") == [1, 2, 3]

