with open("input_06.txt", "r") as f:
    list = f.read().split("\n\n")

    count = 0
    for answergroup in list:
        answergroup = answergroup.split("\n")
        iterator = iter(answergroup)
        try:
            current = next(iterator)
        except StopIteration:
            continue
        stringSet = set(current)
        for answer in iterator:
            if answer == "":
                continue
            answer = answer.strip("\n")
            answerSet = set(answer)
            stringSet = stringSet.intersection(answerSet)
        count += len(stringSet)
    print("Count of common answers: " + str(count))
