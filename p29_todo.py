from copy import deepcopy

def add_task(tasks, title):
    return tasks + [{"title": title, "done": False}]

def complete_task(tasks, index):
    result = deepcopy(tasks)
    result[index]["done"]=True
    return result

def active_tasks(tasks):
    result = []
    for i in range(len(tasks)):
        if tasks[i]["done"] == False:
            result.append(tasks[i]["title"])
    return result

if __name__=="__main__":
    tasks = []
    tasks = add_task(tasks, "learn python")
    tasks = add_task(tasks, "practice loops")
    assert active_tasks(tasks) == ["learn python", "practice loops"]

    done_tasks = complete_task(tasks, 0)
    assert active_tasks(done_tasks) == ["practice loops"]
    assert active_tasks(tasks) == ["learn python", "practice loops"]

