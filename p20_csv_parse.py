import csv

def parse_score_csv(path):
    result = {}
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for line in reader:
            result[line[0]] = int(line[1])
    return result

if __name__ == "__main__":
    with open("scores_test.csv", "w", encoding="utf-8") as f:
        f.write("Alice,90\nBob,80\n")

    assert parse_score_csv("scores_test.csv") == {"Alice": 90, "Bob": 80}
