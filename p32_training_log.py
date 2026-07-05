def best_epoch(logs):
    max_epoch = logs[0]["epoch"]
    max_acc = logs[0]["accuracy"]
    for i in range(len(logs)):
        if logs[i]["accuracy"] > max_acc:
            max_acc, max_epoch = logs[i]["accuracy"], logs[i]["epoch"]
    return max_epoch

def loss_decreased_every_epoch(logs):
    temp = logs[0]["loss"]
    for i in range(1, len(logs)):
        if logs[i]["loss"] >= temp:
            return False
        temp = logs[i]["loss"]
    return True

if __name__ == "__main__":
    logs = [
        {"epoch": 1, "loss": 0.9, "accuracy": 0.6},
        {"epoch": 2, "loss": 0.7, "accuracy": 0.75},
        {"epoch": 3, "loss": 0.5, "accuracy": 0.72},
    ]

    assert best_epoch(logs) == 2
    assert loss_decreased_every_epoch(logs) is True
    assert loss_decreased_every_epoch([{"epoch": 1, "loss": 0.5}, {"epoch": 2, "loss": 0.5}]) is False
