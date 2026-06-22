def average_score(scores):
    result = 0
    if scores:
        for i in scores:
            result += i
        result /= len(scores)
    return result

def best_student(score_dict):
    best_score=0
    best_stu=None
    for i in score_dict.keys():
        if score_dict[i] > best_score:
            best_score = score_dict[i]
            best_stu = i
    return best_stu

def pass_students(score_dict, pass_score):
    result=[]
    for i in score_dict.keys():
        if score_dict[i] >= pass_score: result.append(i)
    return result

if __name__ == "__main__":
    scores = {"Alice": 90, "Bob": 75, "Cindy": 88}
    assert average_score([90, 80, 70]) == 80
    assert average_score([]) == 0
    assert best_student(scores) == "Alice"
    assert best_student({}) is None
    assert pass_students(scores, 80) == ["Alice", "Cindy"]
