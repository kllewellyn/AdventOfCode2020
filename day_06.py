with open("input_06.txt", "r") as f:
    list = f.read().split("\n\n")

    count = 0
    for answergroup in list:
        answergroup = answergroup.replace("\n", "")
        count += len(set(answergroup))

    print("Count of answers: " + str(count))
