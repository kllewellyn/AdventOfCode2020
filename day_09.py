def isValid(input, target):
    count = 0
    for number in input:
        difference = target - int(number.rstrip())
        if (str(difference)+"\n") not in input:
            count += 1
            continue
    if count == len(input):
        return target
    else:
        return 0

with open("input_09.txt", "r") as f:
    list = f.readlines()

    window = 25
    index = 26
    while index < len(list):
        number = int(list[index].rstrip())
        startIndex = index - window
        sublist = list[startIndex:index]
        valid = isValid(sublist, number)
        if valid != 0:
            print("This number is not valid: " + str(valid))
        index += 1
