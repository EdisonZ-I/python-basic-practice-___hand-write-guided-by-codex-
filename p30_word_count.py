def word_count(text):
    temp = text.lower().split()
    result = {}
    for i in temp:
        try:
            result[i]+=1
        except:
            result[i]=1
    return result

def top_k_words(text, k):
    rank = word_count(text)
    count = k
    result=[]
    while (count > 0) and rank != {}:
        max_value = list(rank.values())[0]
        max_key = 0
        for i in range(len(rank)):
            if list(rank.values())[i] > max_value:
                max_value, max_key = list(rank.values())[i], i
        result.append(list(rank.keys())[max_key])
        del rank[list(rank.keys())[max_key]]
        count -= 1
    return result

if __name__ =="__main__":
    assert word_count("AI ai Python") == {"ai": 2, "python": 1}
    assert top_k_words("a b a c b a", 2) == ["a", "b"]
    assert top_k_words("", 3) == []


