def clean_records(records):
    result=[]
    for i in range(len(records)):
        result.append({})
        try:
            result[i]["name"]=records[i]["name"].strip()
            result[i]["age"]=int(records[i]["age"])
            result[i]["score"]=float(records[i]["score"])
        except:
            del result[-1]
    return result

if __name__ == "__main__":
    records = [
        {"name": " Alice ", "age": "20", "score": "88.5"},
        {"name": "Bob", "age": "bad", "score": "70"},
    ]

    assert clean_records(records) == [{"name": "Alice", "age": 20, "score": 88.5}]
